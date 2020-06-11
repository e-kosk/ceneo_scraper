import requests
from bs4 import BeautifulSoup

from scrapper_app.functions import extract_feature, clean_string

from scrapper_app.models import OpinionModel, ProductModel


def get_opinions(product):

    url_host = 'https://www.ceneo.pl/'
    url_postfix = '#tab=rewievs'
    url = url_host + product.product_id + url_postfix
    opinions_amount = 0

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
            features['recommendation'] = True if features['recommendation'] == 'Polecam' else False if features['recommendation'] == 'Nie polecam' else None

            features['product'] = product

            OpinionModel.objects.create(**features)
            opinions_amount += 1

        try:
            url = url_host + soup.select('a.pagination__next').pop(0)['href']
        except IndexError:
            url = None


def get_product(product_id):

    url_host = 'https://www.ceneo.pl/'
    url = url_host + product_id

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        product_name = soup.select('h1.product-name').pop().text.strip()
    except IndexError:
        return None

    product = ProductModel.objects.get_or_create(product_id=product_id, name=product_name)[0]

    return product
