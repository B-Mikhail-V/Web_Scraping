import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

request_url = requests.get(url)
soup = BeautifulSoup(request_url.text, 'html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')
for article in articles:
    article_texts = article.find_all('p', class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    article_texts = [article_text.text.strip() for article_text in article_texts]
    print(article)
