from bs4 import BeautifulSoup
from datetime import datetime as dt
import requests
import json
import re
import sys

def get_news_links(source):
    """
        returns relevant article links from specified source
    """
    if source == 'seekingalpha':
        url = 'https://seekingalpha.com/market-news'
        attributes = {'href':re.compile('/news/*')}
        link_prefix = 'https://seekingalpha.com'
    if source == 'cnbc':
        url = 'https://www.cnbc.com/trader-talk/'
        attributes = {'class':'Card-mediaContainer'}
        link_prefix = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')

    news_links = [f'{link_prefix}{link["href"]}' for link in soup.find_all('a',attributes)]
    return news_links

def article_summaries(source):
    """
        returns article summaries from specifed source
    """
    links = get_news_links(source)
    summaries = {}
    for link in links:
        article = {}
        response = requests.get(link)
        soup = BeautifulSoup(response.text,'lxml')
        if source == 'cnbc':
            bullet_points = soup.find_all('div',{'class':'RenderKeyPoints-list'})
            article_title = soup.find('h1',{'class':'ArticleHeader-headline'}).text
        if source == 'seekingalpha':
            bullet_points = soup.find_all('p',{'class':'bullets_li'})
            article_title = soup.find('h1').text
        if bullet_points:
            bullet_points = [article.text.replace('\xa0',' ') for article in bullet_points]
        else:
            bullet_points = ["No summary available"]
        article_date = soup.find('time')
        if article_date:
            if source == 'cnbc':
                article_date = str(dt.strptime(link[21:31],'%Y/%m/%d'))[:10]
            if source == 'seekingalpha':
                article_date = str(dt.strptime(article_date.text[:13],'%b. %d, %Y'))[:10]
        article['source'] = source
        article['date'] = article_date
        article['summary'] = bullet_points
        summaries[article_title] = article
    return summaries

