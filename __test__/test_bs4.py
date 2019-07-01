from bs4 import BeautifulSoup

html = '''<td class="title">
<div class="tit3" id="ss">
<a href="/movie/bi/mi/basic.nhn?code=164125" title="엑스맨: 다크 피닉스">엑스맨: 다크 피닉스</a>
</div>
</td>'''

# 1. tag 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)
    # print(type(bs))

    tag = bs.td.div.a.text
    print(tag)
    print(type(tag))


# 2. 속성값(attribute) 값 가져오기
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])

    tag = bs.div
    #에러
    print(tag['id'])


# attribute로 태그 조회()
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('td', attrs={'class': 'title'})
    print(tag)

    tag = bs.find(sttrs={'class', 'tit3'})
    print(tag)


if __name__ == '__main__':
    # ex1()
    # ex2()
    ex3()