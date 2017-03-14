# a simple web crawler to crawel MYEGY main pages

import requests
from bs4 import BeautifulSoup

usrInput = int(input('Enter How many pages you like to crawl: '))


def wordList(maxPage):
    page = 1
    with open('site_content.txt', 'w') as content:

        while page <= maxPage:
            url = 'http://myegy.tv/?page=' + str(page)
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')
            currentPage = '=========The Current Page is => ' + str(page) + '========='
            content.write(currentPage)  # writes where you are before each page
            content.write('\n')

            for text in soup.findAll('span', {'class': 'title'}):
                txt = text.string  # grabs only the string from the html code
                content.write('\n')

                for w in txt:
                    content.write(w)
            content.write('\n')
            content.write('\n')
            page += 1
    content.close()


wordList(usrInput)
