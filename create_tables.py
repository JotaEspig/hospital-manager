from config.config import db
from models import *


if __name__ == "__main__":
    db.create_all()
    