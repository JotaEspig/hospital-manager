from config.config import db
from models import * # Gets the models to "db.create_all()" create


if __name__ == "__main__":
    db.create_all()

    if admin.Admin.query.filter_by(username="admin").first() != None:
        exit(0)
    
    a = admin.Admin(username="admin", pwhash="admin") # TODO MUDAR ISSO
    db.session.add(a)
    db.session.commit()
    