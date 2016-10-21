import requests
from bs4 import BeautifulSoup

SITE = 'http://fs.to'


def film_spider(max_page):
    page = 0
    while page <= max_page:
        url = SITE + '/video/films/?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('a', {'class': 'b-poster-tile__link'}):
            href = SITE + link.get('href')
            title = link.find('span', {'class': 'b-poster-tile__title-full'}).string
            vote_ok = link.find('span', {'class': 'b-poster-tile__title-info-vote-positive'}).string
            vote_bad = link.find('span', {'class': 'b-poster-tile__title-info-vote-negative'}).string
            print(vote_ok, '\t', vote_bad, '\t',  title, '\t', href)
        page += 1


film_spider(10)