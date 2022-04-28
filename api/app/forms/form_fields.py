from wtforms import StringField, SelectField, SubmitField, FloatField, IntegerField, \
    BooleanField, TextAreaField, FormField, SelectMultipleField, widgets, FieldList, Form, FileField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Regexp, Length


fields = {

    '_subfund_id' : StringField("Subfund id"),
    'transaction_type': SelectField("Transaction type", choices=['Investment', 'Divestment']),
    'asset_name': StringField('Asset Name'),
    'transaction_value': FloatField('Transaction Amount'),
    'asset_loc': StringField('Asset location'),
    'asset_leverage': FloatField('Asset leverage (new or outstanding in %)'),
    'capital_call_time': SelectField('Capital call type', choices= [('Immediate', 'Deferred')]),
    'liquidity_type': SelectField('Asset liquidity type', choices=['Liquid', 'Semi-liquid', 'Illiquid'])

}