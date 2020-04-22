#!/usr/bin/env python3

# Author: Jeremy Jess
# Email: jeremytjess@gmail.com

import json
import plotly

import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objs as go
import plotly.subplots as subplots

def get_historical_data(ticker,period='1d',interval='1m'):
    """get historical data for stock from given vals

        Parameters
        -----------
        ticker: str
            stock ticker
        period: str ['1d','5d','1mo','3mo','6mo','1y','2y','5y,'10y','ytd','max']
            period for stock history
        interval: str ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo']
    """

    data = yf.download(ticker,period=period,interval=interval)
    data['Close'] = data['Adj Close']
    del data['Adj Close']

    data['10sma'] = data['Close'].rolling(10).mean()
    data['20sma'] = data['Close'].rolling(20).mean()
    return data


def plot_historical_data(df,title):
    """plots historical data from close and 10/20 sma"""
    close_trace = go.Scatter(
        x=df.index,
        y=df['Close'],
        name='Price'
    )
    sma10_trace = go.Scatter(
        x=df.index,
        y=df['10sma'],
        name='10 Min Avg'
    )
    sma20_trace = go.Scatter(
        x=df.index,
        y=df['20sma'],
        name='20 Min Avg'
    )

    traces = [close_trace,sma10_trace,sma20_trace]

    fig = dict(
        data=traces,
	layout={'title':title,
                'paper_bgcolor':'rgba(0,0,0,0)',
                'plot_bgcolor':'rgba(0,0,0,0)'}
    )

    json_fig = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return json_fig

def plot_indexes():
    """plots index graph for the day"""


    dji_df = get_historical_data('^DJI')
    sp_df = get_historical_data('^DJI')
    nasdaq_df = get_historical_data('^DJI')

    dji_fig = plot_historical_data(dji_df,'Dow Jones')
    sp_fig = plot_historical_data(sp_df,'S&P 500')
    nasdaq_fig = plot_historical_data(nasdaq_df,'Nasdaq')

    return [dji_fig,sp_fig,nasdaq_fig]


