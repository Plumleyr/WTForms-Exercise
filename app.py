from flask import Flask
from models import db, connect_db
from routes import routes_bp

app = Flask(__name__)

app.register_blueprint(routes_bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)

app.config["SECRET_KEY"] = "ZZZZZ"


