from books import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    series = db.Column(db.String(100))
    no_of_books_in_series = db.Column(db.Integer)
    book_in_series = db.Column(db.String(100))
    book_image = db.Column(db.String(20), default='default.jpg')

    def __repr__(self):
        return self.title
