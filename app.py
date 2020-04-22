#!/usr/bin/env python3

# Author: Jeremy Jess
# Email: jeremytjess@gmail.com

from flask import Flask,render_template,request

import financial_info
import plotly
import util

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def home_page():
    ids = ['Dow Jones','S&P 500','Nasdaq']

    index_graphs = financial_info.plot_indexes()
    search_form = util.TickerForm()

    if request.method == 'GET':
        ticker = 'SPY'
        period = '1d'
    else:
        ticker = request.form['search']
        period = request.form['select']
    ticker_df = financial_info.get_historical_data(ticker,period)
    ticker_graph = financial_info.plot_historical_data(ticker_df,ticker)
    return render_template('index.html',
                               ids=ids,
                               stock_id=ticker,
                               index_graphs=index_graphs,
                               stock_graph=ticker_graph,
                               form=search_form)











if __name__ == '__main__':
    app.run(debug=True)
