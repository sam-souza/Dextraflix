from flask import Flask
from flask_pymongo import PyMongo
from views.categoria import categorias_bp
from views.usuario import usuarios_bp

app = Flask(__name__)

app.register_blueprint(categorias_bp)
app.register_blueprint(usuarios_bp)

app.config["MONGO_URI"] = "mongodb://localhost:27017/dextraflix"
mongo = PyMongo(app)



