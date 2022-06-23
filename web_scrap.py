import requests
from bs4 import BeautifulSoup

base_url = 'https://habr.com'
url = base_url + '/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'проект', 'Android', 'продукт']
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
}

request_url = requests.get(url, headers=headers)
soup = BeautifulSoup(request_url.text, 'html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')
result = {}
for article in articles:
    article_texts = article.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    article_texts = [article_text.text.strip() for article_text in article_texts]
    for art_text in article_texts:
        for keyword in KEYWORDS:
            if keyword in art_text:
                data_pub = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['datetime'][:10]
                article_title = article.find('a', class_='tm-article-snippet__title-link').find('span').text
                article_href = article.find('a', class_='tm-article-snippet__title-link').attrs['href']
                article_link = base_url + article_href
                result_list = [data_pub, article_title, article_link]
                result[article_title] = result_list



for val in result.values():
    print(val)

