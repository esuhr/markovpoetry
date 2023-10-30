from flask import request, jsonify
from flask_cors import cross_origin
from models import Poem, poems_schema
from config import app

@app.route('/')
def index():
    output = []
    return output

@app.route('/poems', methods=['GET'])
@cross_origin()
def get_poems():
    # get poems based on author and a date range
    authors = request.args.get('authors')
    authors = authors.split(',') if authors else None

    dates = request.args.get('dates')
    dates = dates.split(',') if dates else None
    dates = [int(date) for date in dates] if dates else None
    start = min(dates) if dates else None
    end = max(dates) if dates else None

    if not authors and not dates:
        poems = Poem.query.with_entities(Poem.poem_clean, Poem.author, Poem.date).all()
    elif not authors:
        poems = Poem.query.filter(Poem.date >= start, Poem.date <= end).with_entities(Poem.poem_clean, Poem.author, Poem.date).all()
    elif not dates:
        poems = Poem.query.filter(Poem.author.in_(authors)).with_entities(Poem.poem_clean, Poem.author, Poem.date).all()
    else:
        poems = Poem.query.filter(Poem.author.in_(authors), Poem.date >= start, Poem.date <= end).with_entities(Poem.poem_clean, Poem.author, Poem.date).all()

    result = poems_schema.dump(poems)
    return jsonify(result)

@app.route('/authors', methods=['GET'])
def get_authors():
    authors = Poem.query.with_entities(Poem.author).distinct()
    author_list = [author[0] for author in authors]
    return jsonify(author_list)

@app.route('/dates', methods=['GET'])
# get min and max dates
def get_dates():
    dates = Poem.query.with_entities(Poem.date)
    date_list = [date[0] for date in dates if date[0] is not None]
    dateminmax = [min(date_list), max(date_list)]
    return jsonify(dateminmax)
    

if __name__ == '__main__':
    app.run(port=8000, debug=True)