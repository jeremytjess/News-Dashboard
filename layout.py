import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import util
import news


# elements
news = html.Div([
        dcc.Tabs(
            id='news-tabs',
            value='cnbc',
            children=[
                dcc.Tab(
                    label='CNBC',
                    value='cnbc'
                ),
                dcc.Tab(
                    label='Seeking Alpha',
                    value='seekingalpha'
                )
            ],
            style=dict(
                float='left'
             )
        ),
        html.Div(
            id='news-content',
            style=dict(
                float='left',
                textAlign='center'
            )
        )
    ])

graph = html.Div([
        dcc.Input(
            id='Ticker',
            value='SPY',
            type='text'
        ),
        html.Button(
            id='submit-button',
            type='submit',
            children='Submit'
        ),
        dcc.Graph(
            id='candlestick-chart',
            figure=dict(
                data=[
                    dict(
                        x=[1,2],
                        y=[3,1]
                    )
                ],
                layout=go.Layout(
                    title='Price History',
                    xaxis=dict(
                            title='Date'
                    ),
                    yaxis=dict(
                    title='Returns',
                    tickformat=".2%"
                    )
                )
            ),style=dict(
                textAlign='center',
                width='100%'
            )
        )
        ],style=dict(
            width='100%'
        ))


# layout
layout = html.Div([
    html.H1('Dashboard',
            style=dict(
                textAlign='center'
            )
    ),
    dcc.Markdown(' --- '),
    html.Div([
        dcc.Tabs(
            id='tabs',
            value='home-tab',
            children=[
                dcc.Tab(
                    label='Home',
                    value='home-tab'
                ),
                dcc.Tab(
                    label='News',
                    value='news-tab'
                )
            ],
            style=dict(
                float='left'
             )
        ),
        html.Div(
            id='tab-content',
            style=dict(
                textAlign='center',
                width='100%'
            ),
            children=[graph,news],
        )
    ])
])

