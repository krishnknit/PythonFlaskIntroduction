from project import db
#from project.models import BlogPost

# create the database and the db tables
db.create_all()


# insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Flask", "discover flask.com"))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("mysql", "we set the local mysql instance."))

# commit the changes
db.session.commit()