from bs4 import BeautifulSoup
import requests
import re
import types

data = requests.get('https://jamesclear.com/new-habit')
soup = BeautifulSoup(data.content, 'html.parser')


HEADER_TAGS = ['h2', 'h3', 'h4', 'h5', 'h6']

articleData: BeautifulSoup = soup.find('article')

print(articleData.find_all('h1'))

header: BeautifulSoup
for header in articleData.find_all(HEADER_TAGS):
    replacement = soup.new_tag('h1')
    replacement.string = header.string
    header.replace_with(replacement)

print(articleData)
