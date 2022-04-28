from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from api.app.forms import form_content, form_fields


def new_transaction_model():
    class TransactionForm(FlaskForm):

        for k in form_content.transaction_args:
            # equivalent to 'name= StringField("Trade Id", default=default_values['trade_id'])'
            locals()[k] = form_fields.fields[k]
            # make fund_name a Selectfield

    transaction_form = TransactionForm()

    return transaction_form