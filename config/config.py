import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS # permitir back receber json do front
from flask_login import LoginManager


# configurações
app = Flask(__name__)
CORS(app) # aplicar o cross domain
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.join(path, "../")
arquivobd = os.path.join(root_path, 'db/hospital.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
app.secret_key = os.getenv("SECRET_KEY")
if app.secret_key is None or app.secret_key.strip() == "":
    raise Exception("secret key cannot be empty. To set a secret key, use: " \
        "'export SECRET_KEY=<your-secret-key>'")
