import pandas as pd
import pymongo

from api.app import mongodb
import datetime as dt
import dateutil.parser

db = mongodb['myDatabase']

def date_adj(date):

    now = date
    year = now.year
    month = now.month
    day = now.day
    dateStr = str(year) + "-" + str(month) + "-" + str(day)

    return dateStr


def update_cf(_id = None, collection = 'deals'):

    """
    Each transaction is to be recorded as capital call (Acquisition) or distribution (Divestment)
    Reported NAVs to be stored separately

    :param _id: subfund if in mongo db
    :param collection: collection of deals
    :return: stream of cashflows for IRR calculation or other analytics --> feed realized cfs into our db improve JCurve model
    """
    dict = {}
    coll = db[collection]

    cursor_cf = coll.find({}).sort('date', pymongo.ASCENDING)
    for k in cursor_cf:
        dict[k['date']] = k['transaction_value']

    data = pd.Series(dict)

    return data


