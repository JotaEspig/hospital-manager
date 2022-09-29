from config.config import db
from models import * # Gets the models to "db.create_all()" create


if __name__ == "__main__":
    db.create_all()
    