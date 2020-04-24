import dash
import layout
import elements
import candlestick

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from dash.dependencies import Input, Output, State
from dash_table import DataTable
from datetime import datetime as dt

app = dash.Dash()

app.layout = layout.layout


# callbacks
@app.callback(Output('tab-content','children'),
              [Input('tabs','value')])
def render_content(tab):
    """renders display based on tab"""
    if tab == 'home-tab':
        return layout.graph
    elif tab == 'news-tab':
        return layout.news

@app.callback(Output('news-content','children'),
              [Input('news-tabs','value')])
def render_news_content(tab):
    """renders specified news source content"""
    if tab == 'cnbc':
        return elements.cnbc_news
    elif tab == 'seekingalpha':
        return elements.seekingalpha_news

@app.callback(Output('candlestick-chart', 'figure'),
	      [Input('submit-button', 'n_clicks')],
                [State('Ticker', 'value')])
def gen_graph(n_clicks,ticker,period='1y',interval='1d'):
    fig = candlestick.plot_historical_data(ticker,period=period,interval=interval)
    return fig






if __name__ == '__main__':
    app.run_server(debug=True)
