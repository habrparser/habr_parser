import requests
from bs4 import BeautifulSoup as BS

a = []

def get_data(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    soup = BS(requests.get(url, headers=headers).text, 'lxml')
    list_of_article = soup.find('div', class_='tm-articles-list')
    articles = list_of_article.find_all('article', class_='tm-articles-list__item')
    for article in articles:
        
        try:
            title = article.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').text
        except:
            title = "not found"
        
        try:
            themes = article.find('div', class_='tm-article-snippet__hubs').text
        except:
            themes = "not found"
        
        try:
            img = article.find('img', class_='tm-article-snippet__lead-image').get("src")
        except:
            img = 'Not found'
        
        try:
            text = article.find('div', class_='article-formatted-body article-formatted-body_version-2').text
        except:
            text = 'not found'
        
        try:
            created_at = article.find('span', class_='tm-article-snippet__datetime-published').text
        except:  
            created_at = 'not found'
        try:
            author = article.find('a', class_='tm-user-info__username').text
        except:
            author = 'not found'

        data = {'title': title,
                'themes': themes,
                'image': img,
                'text': text,
                'created_at':created_at,
                'author': author
                }

    a.append(data)
    return a


def main():
    for i in range(1, 30):
        url = f'https://habr.com/ru/all/page{i}/'
        data = get_data(url) 
    return data

        