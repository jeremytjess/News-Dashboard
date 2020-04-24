import dash_core_components as dcc
import dash_html_components as html

def gen_article_div(articles):
    """creates dash Div with article & summary"""
    elems = []
    for article in articles:
        bullet_points = [html.Li(art) for art in articles[article]['summary'] if art]
        elem = html.Ul([
                html.H2(article),
                html.H3(articles[article]['source']),
                html.H3(articles[article]['date']),
                html.P(bullet_points)
                ],style=dict(
                    listStylePosition='inside',
                    #display='inline-block',
                    textAlign='left'
                ))
        elems.append(elem)
    return html.Div(elems)
