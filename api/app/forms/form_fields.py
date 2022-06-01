from wtforms import StringField, SelectField, DateField, DateTimeField, SubmitField, FloatField, IntegerField, \
    BooleanField, TextAreaField, FormField, SelectMultipleField, widgets, FieldList, Form, FileField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Regexp, Length

from api.app import mongodb
import pymongo

import datetime as dt

db = mongodb['myDatabase']
coll = db['deals']

def fund_list(coll):

    final_list = []
    for k in coll.find():
        final_list.append((k['asset_id'], k['asset_name']))

    return final_list



fields = {

    '_subfund_id' : StringField("Subfund id"),
    'transaction_type': SelectField("Transaction type", choices=['Investment', 'Divestment']),
    'asset_name': StringField('Asset Name'),
    'transaction_value': FloatField('Transaction Amount'),
    'asset_loc': StringField('Asset location'),
    'asset_leverage': FloatField('Asset leverage (new or outstanding in %)'),
    'capital_call_time': SelectField('Capital call type', choices= [('Immediate', 'Deferred')]),
    'liquidity_type': SelectField('Asset liquidity type', choices=['Liquid', 'Semi-liquid', 'Illiquid']),
    'date': DateTimeField('Date', default = dt.datetime.today().replace(microsecond=0)),
    'upload_memo': FileField('Investment Memo Upload'),
    'funds': SelectField('Choose your subfund', choices  = fund_list(coll)),
}
