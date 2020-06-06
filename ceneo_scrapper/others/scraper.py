import requests
from bs4 import BeautifulSoup

from classes import Opinion
from functions import save_to_file, extract_feature, clean_string

url_host = 'https://www.ceneo.pl/'
product_id = input('Product ID: ') or '47044569'
url_postfix = '#tab=rewievs'
url = url_host + product_id + url_postfix
all_opinions = []

selectors = {
    'author': ['span.user-post__author-name'],
    'recommendation': ['span.user-post__author-recomendation > em'],
    'stars': ['span.user-post__score-count'],
    'content': ['div.user-post__text'],
    'cons': ['div.review-feature__col:has(> div.review-feature__title--negatives)'],
    'pros': ['div.review-feature__col:has(> div.review-feature__title--positives)'],
    'useful': ['button.vote-yes > span'],
    'useless': ['button.vote-no > span'],
    'opinion_date': ['span.user-post__published > time:nth-child(1)', 'datetime'],
    'purchase_date': ['span.user-post__published > time:nth-child(2)', 'datetime'],
}


while url:

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    opinions = soup.select('div.js_product-review')

    for opinion in opinions:
        features = {key: extract_feature(opinion, *args) for key, args in selectors.items()}

        features['opinion_id'] = int(opinion['data-entry-id'].strip())
        features['stars'] = float(features['stars'].split('/')[0].replace(',', '.'))
        features['useful'] = int(features['useful'])
        features['useless'] = int(features['useless'])
        features['content'] = clean_string(features['content'], {'\n': ', ', '\r': ''})
        features['pros'] = clean_string(features['pros'], {'\n': ', ', '\r': '', 'Zalety, ': ''})
        features['cons'] = clean_string(features['cons'], {'\n': ', ', '\r': '', 'Wady, ': ''})

        all_opinions.append(Opinion(**features))

    try:
        url = url_host + soup.select('a.pagination__next').pop(0)['href']
    except IndexError:
        url = None

save_to_file(all_opinions, product_id)
