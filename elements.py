import dash_core_components as dcc
import dash_html_components as html
import news
import util
import dashboard

# news content
cnbc_summaries = news.article_summaries('cnbc')
seekingalpha_summaries = news.article_summaries('seekingalpha')

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


cnbc_news = html.Div([
    util.gen_article_div(cnbc_summaries)
])

seekingalpha_news = html.Div([
    util.gen_article_div(seekingalpha_summaries)
])
