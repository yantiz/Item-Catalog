from database_setup import db, Category, Item

category_1 = Category(name='Kitchen')
category_2 = Category(name='Firearm')
category_3 = Category(name='Vehicle')

db.session.add(category_1)
db.session.add(category_2)
db.session.add(category_3)

db.session.commit()
