from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///item_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Category(db.Model):
    __tablename__ = 'category'

    name = db.Column(db.String(80), primary_key=True)


class Item(db.Model):
    __tablename__ = 'item'

    name = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    category_name = db.Column(db.String, db.ForeignKey('category.name'))
    user_id = db.Column(db.String, db.ForeignKey('user.id'))
    created = db.Column(db.DateTime, nullable=False,
                        server_default=db.func.now())

    category = db.relationship(
                           'Category',
                           backref=db.backref('items', order_by=created.desc())
                              )
    user = db.relationship(
                          'User',
                          backref=db.backref('items', order_by=created.desc())
                          )

    @property
    def serialize(self):
        return {
                'name': self.name,
                'description': self.description,
                'category_name': self.category_name,
                'user_id': self.user_id
               }

db.create_all()
