import sys
import time
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen
import ssl

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from collection import crawler


def crawling_pelicana():
    results = []

    for page in count(1):
        url = 'https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % (page)
        html = crawler.crawling(url)
        if html is False:
            continue

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sido, gugun = address.split(' ')[:2]
            t = (name, address, sido, gugun)
            results.append(t)

    # for t in results:
    #     print(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/pelicana.csv', encoding='utf-8', mode='w', index=True)
    print(table)


# 과제임
def crawling_nene():
    results = []
    prename = ''

    for page in range(1, 5):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?ex_select=1&ex_select2=&IndexSword=&GUBUN=A&page=%d' % (page)
        html = crawler.crawling(url)
        if html is False:
            continue

        bs = BeautifulSoup(html, 'html.parser')
        divs = bs.findAll('div', attrs={'class': 'shopInfo'})

        # 마지막페이지 체크
        div = bs.find('div', attrs={'class': 'shopInfo'})
        name = div.find('div', attrs={'class': 'shopName'}).text
        if prename == name:
            break
        prename = name

        for div in divs:
            name = div.find('div', attrs={'class': 'shopName'}).text
            address = div.find('div', attrs={'class': 'shopAdd'}).text
            sido, gugun = address.split(' ')[:2]
            t = (name, address, sido, gugun)
            results.append(t)

    # for t in results:
    #     print(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/nene.csv', encoding='utf-8', mode='w', index=True)
    print(table)


def crawling_kyochon():
    results = []
    for sido1 in count(1):
        url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=&txtsearch=' % (sido1)
        html = crawler.crawling(url)
        if html is False:
            break

        for sido2 in count(1):
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' % (sido1, sido2)
            html = crawler.crawling(url)

            if html is False:
                break
            print(sido1, sido2, sep=' / ')
            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs={'class': 'list'})

            tag_spans = tag_ul.findAll('span', attrs={'class': 'store_item'})

            for tag_span in tag_spans:
                strings = list(tag_span.strings)
                name = strings[1]
                address = strings[3].replace('\r\n\t', '').strip()
                sidogu = address.split()[:2]

                results.append((name, address) + tuple(sidogu))

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/kyochon.csv', encoding='utf-8', mode='w', index=True)
    print(table)


def crawling_goobne():
    results = []

    url = 'http://goobne.co.kr/store/search_store.jsp'
    wd = webdriver.Chrome('D:/cafe24/chromedriver_win32/chromedriver.exe')
    wd.get(url)
    time.sleep(2)

    for page in count(1):
        script = 'javascript:store.getList(\'%d\');' % (page)

        wd.execute_script(script)
        time.sleep(1)

        html = wd.page_source
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody', attrs={'id': 'store_list'})
        tag_trs = tag_tbody.findAll('tr')

        # 마지막 검출
        if tag_trs[0].get('class') is None:
            break;

        for tag_tr in tag_trs:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]
            sidogu = address.split()[:2]

            results.append((name, address) + tuple(sidogu))

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/goobne.csv', encoding='utf-8', mode='w', index=True)
    print(table)

    wd.quit()


if __name__ == '__main__':
    # crawling_pelicana()

    # 과제
    crawling_nene()
    # crawling_kyochon()
    # crawling_goobne()
