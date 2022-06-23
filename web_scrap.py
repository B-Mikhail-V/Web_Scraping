import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'проект', '3D']
headers = {
    'authority': 'www.kith.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

request_url = requests.get(url, headers=headers)
soup = BeautifulSoup(request_url.text, 'html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')
for article in articles:
    article_texts = article.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    article_texts = [article_text.text.strip() for article_text in article_texts]
    for text in article_texts:
        for keyword in KEYWORDS:
            if keyword in text:
                print(f'найдено {keyword} в: {text}')

            else:
                print(f'слово {keyword} не найдено')
