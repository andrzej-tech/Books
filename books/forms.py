from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField,IntegerField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    series = StringField('series', validators=[DataRequired()])
    no_of_books_in_series = IntegerField('no_of_books_in_series', validators=[DataRequired()])
    book_in_series = StringField('book_in_series', validators=[DataRequired()])
    book_image = FileField('book_image', validators=[FileAllowed(["jpg", "png", "jfif"])])
    submit = SubmitField('Post')