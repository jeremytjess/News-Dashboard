import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.subplots import make_subplots
import json
import plotly

def plot_historical_data(ticker,period,interval):
    """gets historical data for specified
        period and interval"""
    df = yf.download(ticker,period=period,interval=interval)

    df['Close'] = df['Adj Close']

    df['10sma'] = df['Close'].rolling(10).mean()
    df['20sma'] = df['Close'].rolling(20).mean()

    candle_trace = go.Candlestick(
        x=df.index,
        open=df['Open'],
        close=df['Close'],
        low=df['Low'],
        high=df['High'],
        name='Candlestick',
        yaxis='y2'
    )

    sma10_trace = go.Scatter(
        x=df.index,
        y=df['10sma'],
        name='10 Day SMA',
        yaxis='y2',
        mode='lines',
        line_color='blue',
        hoverinfo='skip'
    )
    sma20_trace = go.Scatter(
        x=df.index,
        y=df['20sma'],
        name='20 Day SMA',
        yaxis='y2',
        mode='lines',
        line_color='orange',
        hoverinfo='skip'
    )
    """
    volume_trace = go.Bar(
        x=df.index,
        y=df['Volume'],
        name='Volume',
        yaxis='y'
    )

    rangeselector=dict(
        visible=True,
        x=0,
        y=0.9,
        bgcolor='rgba(150,200,250,0.4)',
        font=dict(size=13),
        buttons=list([
                    dict(
                        count=1,
                        label='reset',
                        step='all'
                    ),
                    dict(
                        count=1,
                        label='1yr',
                        step='year',
                        stepmode='backward'
                    ),
                    dict(
                        count=6,
                        label='6 mo',
                        step='month',
                        stepmode='backward'
                    ),
                    dict(
                        count=1,
                        label='1 mo',
                        step='month',
                        stepmode='backward'
                    ),
                    dict(
                        count=5,
                        label='5 day',
                        step='day',
                        stepmode='backward'
                    ),
                    dict(
                        step='all'
                    )
        ])
    )


    traces = [candle_trace,sma10_trace,sma20_trace,volume_trace]
    layout = {
        'title':ticker,
        'xaxis':{
            'rangeselector':rangeselector
        },
        'yaxis':{
            'showticklabels':False,
            'fixedrange':True
        },
        'yaxis2':{
            'domain':[0.2,0.8],
            'autorange':True,
            'fixedrange':False,
        },
        'margin':{
            't':40,
            'b':40,
            'r':40,
            'l':40
        },
    }
    """
    traces = [candle_trace,sma10_trace,sma20_trace]
    layout = {
        'title':{
            'text':f'{ticker} Price History',
            'xanchor':'center'
        },
        'yaxis':{
            'fixedrange':False
        },
        'hovermode':'closest'
    }
    fig = go.Figure(
        data=traces,
        layout=layout
    )

    return fig

