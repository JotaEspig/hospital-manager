from config.config import db
import models # Gets the models to "db.create_all()" create


if __name__ == "__main__":
    db.create_all()

    if models.admin.Admin.query.filter_by(username="admin").first() != None:
        exit(0)

    a = models.admin.Admin(username="admin", pwhash="admin")
    db.session.add(a)
    db.session.commit()
    