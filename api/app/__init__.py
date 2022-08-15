from flask import Flask
import pymongo
from dotenv import load_dotenv, dotenv_values
import os
from flask_ckeditor import CKEditor

ckeditor = CKEditor()
mongodb = None
a = os.getcwd()
print(a)
config = dotenv_values(".env")

def init_app():

    global mongodb

    app = Flask(__name__, static_folder='static')

    ckeditor.init_app(app)
    mongodb = pymongo.MongoClient(config['URI'])
    from .transaction import transaction_bp
    app.register_blueprint(transaction_bp)

    return app