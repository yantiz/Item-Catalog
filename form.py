from database_setup import Category

categories = Category.query.order_by(Category.name)
category_choices = [(category.name, category.name) for category in categories]
category_choices = category_choices

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), 
                                           Regexp(r'^[a-zA-Z\s]*$'),
                                           Length(max=80)])
    description = TextAreaField('Description', validators=[DataRequired()])
    category = SelectField('Category', choices=category_choices)
    submit = SubmitField('Submit')
