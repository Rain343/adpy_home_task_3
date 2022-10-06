import bs4
import requests


HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
URL = 'https://habr.com'
# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']


response = requests.get(URL, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')


articles = soup.find_all('article')
for article in articles:
    article_id = article.get('id')

    response = requests.get(f'{URL}/ru/post/{article_id}', headers=HEADERS)
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')

    full_article = soup.find(id='post-content-body')

    for keyword in KEYWORDS:
        if keyword in full_article.text:
            date = article.find('time').get('title')
            title = article.find(class_='tm-article-snippet__title-link').text
            link = article.find(class_='tm-article-snippet__title-link').get('href')
            print(date, title, link)
            break