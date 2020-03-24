#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

def get_words():
    # get the content of webpage
    respond = requests.get("https://www.globalrelay.com/*", verify=False, allow_redirects=False)
    soup = BeautifulSoup(respond.content)

    # get the words within paragraphs
    text_p = (''.join(s.findAll(text=True)) for s in soup.findAll('p')) 
    c_p = Counter(x.rstrip(punctuation).lower() for y in text_p for x in y.strip())

    # We get the words within divs
    text_div = (''.join(s.findAll(text=True))for s in soup.findAll('div'))
    c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))

    return c_p + c_div


 
def count_words(url, the_word):
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content, 'lxml')
    words = soup.find(text=lambda text: text and the_word in text)
    print(words)
    return len(words)
 
 
def main():
    url = 'https://python-forum.io/Thread-How-to-find-a-specific-word-in-a-webpage-and-How-to-count-it'
    word = 'code'
    count = count_words(url, word)
    print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, word))
 
if __name__ == '__main__':
    main()
