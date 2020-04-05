import requests
from bs4 import BeautifulSoup

from classes import Opinion
from functions import save_to_file

url_host = 'https://www.ceneo.pl'
url_postfix = '/85910996#tab=rewievs'
url = url_host + url_postfix
all_opinions = []


while url:

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    opinions = soup.select('li.js_product-review')

    for opinion in opinions:

        opinion_id = opinion['data-entry-id'].strip()

        author = opinion.select('div.reviewer-name-line').pop().text.strip()

        try:
            recommendation = opinion.select('div.product-review-summary > em').pop().text.strip()
        except IndexError:
            recommendation = None

        stars = opinion.select('span.review-score-count').pop().text.strip()

        content = opinion.select('p.product-review-body').pop().text.strip()

        try:
            cons = opinion.select('div.cons-cell > ul').pop().text.strip()
        except IndexError:
            cons = None

        try:
            pros = opinion.select('div.pros-cell > ul').pop().text.strip()
        except IndexError:
            pros = None

        useful = opinion.select('button.vote-yes > span').pop().text.strip()

        useless = opinion.select('button.vote-no > span').pop().text.strip()

        opinion_date = opinion.select('span.review-time > time:nth-child(1)').pop()["datetime"].strip()

        try:
            purchase_date = opinion.select('span.review-time > time:nth-child(2)').pop()['datetime'].strip()
        except IndexError:
            purchase_date = None

        fields = [opinion_id, author, recommendation, stars, content, cons, pros, useful, useless, opinion_date, purchase_date]
        all_opinions.append(Opinion(*fields))

    try:
        url = url_host + soup.select('a.pagination__next').pop()['href']
    except IndexError:
        url = None

save_to_file(all_opinions)
