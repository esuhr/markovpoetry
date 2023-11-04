from flask import request, jsonify
from flask_cors import cross_origin
from models import Poem, poems_schema
from config import app
from helpers import MarkovModel

model = None

@app.route('/')
def index():
    output = []
    return output

@app.route('/init', methods=['POST'])
@cross_origin()
def initializeModel():
    global model
    poems = Poem.query.with_entities(Poem.poem_clean).all()
    poems = [poem[0] for poem in poems]
    model = MarkovModel(poems)
    return jsonify({'success': True, 'message': 'Model initialized'})

@app.route('/generate', methods=['POST'])
@cross_origin()
def generateText():
    global model
    if not model:
        return jsonify({'success': False, 'message': 'Model not initialized'})
    
    start_word = request.args.get('start_word', default=None)
    num_words = request.args.get('num_words', default=20, type=int)

    if not start_word:
        return jsonify({'success': False, 'message': 'No start word provided'})
    
    words = model.generate_text(start_word, num_words)
    return jsonify({'success': True, 'message': words})

@app.route('/authors', methods=['GET'])
def get_authors():
    authors = Poem.query.with_entities(Poem.author).distinct()
    author_list = [author[0] for author in authors]
    return jsonify(author_list)

@app.route('/corpus/date/<start_date>/<end_date>', methods=['GET'])
# get min and max dates
def get_dates(start_date, end_date):
    dates = Poem.query.with_entities(Poem.date)
    date_list = [date[0] for date in dates if date[0] is not None]
    dateminmax = [min(date_list), max(date_list)]
    return jsonify(dateminmax)
    

if __name__ == '__main__':
    app.run(port=8000, debug=True)