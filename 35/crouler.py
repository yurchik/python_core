import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "lxml")
    for text_news in soup.find_all('div', {'class': 'esc-lead-snippet-wrapper'}):
        content = text_news.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = r'~!@#$%^&*()_+:;"{}\'[]\\|?/.>,<`'
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_counter = {}
    for word in clean_word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    for key, value in sorted(word_counter.items(), key=operator.itemgetter(1)):
        print(key, value)

start('https://news.google.com.ua/')