from flask import Flask
import pymongo
from dotenv import load_dotenv, dotenv_values
import os

mongodb = None
a = os.getcwd()
config = dotenv_values(".env")

def init_app():

    global mongodb

    app = Flask(__name__)

    mongodb = pymongo.MongoClient(config['URI'])
    from .transaction import transaction_bp
    app.register_blueprint(transaction_bp)

    return app