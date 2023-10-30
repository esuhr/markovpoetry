from config import db, ma

# Poem Model
class Poem(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    date = db.Column(db.Integer)
    poem = db.Column(db.Text)
    poem_clean = db.Column(db.Text)
    themes = db.Column(db.String(100))
    forms = db.Column(db.String(100))
    occs = db.Column(db.String(100))

    def __init__(self, title, author, date, poem, poem_clean, themes, forms, occs):
        self.title = title
        self.author = author
        self.date = date
        self.poem = poem
        self.poem_clean = poem_clean
        self.themes = themes
        self.forms = forms
        self.occs = occs

class PoemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Poem
        load_instance = True
        sqla_session = db.session

poem_schema = PoemSchema()
poems_schema = PoemSchema(many=True)