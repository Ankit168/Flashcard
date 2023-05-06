from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import uuid # for public id
from models import *
from  werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
from flask_cors import CORS


from datetime import datetime, timedelta
from api import *
  
# creating the flask app
app = Flask(__name__)
# Db connectioin
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flash-card-v2-database.sqlite3"
db.init_app(app)
app.config['SECRET_KEY'] = 'qwerty'

CORS(app)
jwt = JWTManager(app)
# creating an API object
api = Api(app)
    
# adding the defined resources along with their corresponding urls
api.add_resource(Login,'/login')
api.add_resource(Register,'/Register')
api.add_resource(Decks, "/deck","/deck/<deck_id>")
api.add_resource(Cards, "/card","/card/<card_id>","/deck/<deck_id>/cards")
api.add_resource(Scores, "/score","/deck/<deck_id>/updateScore")
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)