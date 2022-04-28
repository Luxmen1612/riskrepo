from flask import Flask
import pymongo

mongodb = None

def init_app():

    global mongodb

    app = Flask(__name__)
    mongodb = pymongo.MongoClient('mongodb+srv://draths:Bremen92@cluster0.95mle.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    #db = mongodb['myDatabase']
    #coll = db['deals']

    from .transaction import transaction_bp
    app.register_blueprint(transaction_bp)

    return app