from api.app import mongodb
from api.app.transaction import transaction_bp
from api.app.forms.form_models import new_transaction_model
import plotly.express as px
import pandas as pd
from flask import render_template, request, redirect, url_for
import json
import plotly
from plotly.graph_objs import *
import docx
import io
import matplotlib.pyplot as plt
from helpers.cf_analytics import update_cf, date_adj
import datetime as dt

db = mongodb['myDatabase']
coll = db['deals']

@transaction_bp.route("/transaction/dashboard", methods = ["GET", "POST"])
def render_dashboard():

    values = {}
    liquidity = {}
    ptf_count = 0

    for deals in coll.find():

        ptf_count += 1
        values[deals['asset_name']] = deals['transaction_value']
        liquidity[deals['asset_name']] = deals['liquidity_type']

    deals_ser = pd.Series(values)
    liquidity_ser = pd.Series(liquidity)
    cf_data = update_cf().sort_index(ascending=True)

    fig = px.pie(title = 'Asset overview', values = deals_ser, names=deals_ser.index.values)
    fig.update_layout({
        'paper_bgcolor' : 'rgba(0,0,0,0)',
        'plot_bgcolor' : 'rgba(0,0,0,0)'
    })

    fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    fig1 = px.pie(title = 'Liquidity overview', values = liquidity_ser, names = liquidity_ser.index.values)
    fig1 = json.dumps(fig1, cls = plotly.utils.PlotlyJSONEncoder)

    fig4 = px.line(cf_data, title = 'Cashflow')
    fig4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    #fig.show()

    return render_template('dashboard.html', fig = fig, fig1 = fig1, fig4 = fig4, table = [deals_ser.to_frame().to_html(classes = 'data')])

@transaction_bp.route("/render_form", methods = ["GET", "POST"])
def render_form():

    form = new_transaction_model()
    #form['asset_name'].data = 'FundRisQ S.A.' #to be used when pre-filling the form (for example when using a divestment icon next to each asset to prefill form with asset name & divestment flag)

    if request.method == "POST":
        fund_data = form.data.copy()
        if fund_data['transaction_type'] == 'Divestment' and fund_data['transaction_type'] > 0:
            fund_data['transaction_amount'] = - fund_data['transaction_amount']
        #fund_data['date'] = date_adj(fund_data['date'])
        #fund_data['date'] = dt.datetime.today().replace(microsecond=0)
        coll.insert_one(fund_data)

    return render_template('new_transaction.html', form = form)

@transaction_bp.route("/generate_report", methods = ["GET", "POST"])
def generate_report():

    values = {}
    liquidity = {}

    document = docx.Document()

    document.add_heading('Quarterly risk report', 0)
    document.add_heading('Subfund XYZ', 2)

    document.add_paragraph('This risk report provides you with an overview of the subfund"s exposure towards market, credit, liquidity and other risks. Please contact the risk department if you have further questions')

    document.add_paragraph()
    document.add_heading('Portfolio overview', 3)

    for deals in coll.find():

        values[deals['asset_name']] = deals['transaction_value']
        liquidity[deals['asset_name']] = deals['liquidity_type']

    deals_ser = pd.Series(values)
    liquidity_ser = pd.Series(liquidity)

    memfile = io.BytesIO()
    plt.plot(deals_ser)
    plt.savefig(memfile)

    #fig = px.pie(values = deals_ser, names=deals_ser.index.values)
    p = document.add_paragraph()
    r = p.add_run()
    r.add_picture(memfile)

    document.save('riskreport.docx')
    print('Report has been generated')

    return redirect(url_for('transaction_bp.render_dashboard'))










