from bs4 import BeautifulSoup
from lxml import etree
from sphinx.util import requests

def get_cf_rating(name):
    url = "https://codeforces.com/profile/"
    url = url + name
    data = {}
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    res = requests.get(url, data=data, headers=headers)
    # print(res.text)
    html = res.content

    tree = etree.HTML(html)
    value = tree.xpath('//*[@id="pageContent"]/div[2]/div/div[2]/ul/li[1]/span[1]')

    return value[0].text


def slove(datas):
    res = []
    for who,name in datas.items():
        tem = {}
        try:
            print('正在查询'+who)
            rating = get_cf_rating(name)
            rating = int(rating)
            print('查询成功')
        except:
            print('查询失败')
            rating = -1
        tem['姓名']=who
        tem['cf用户名']=name
        tem['cf_Rating']=rating
        res.append(tem)
    return res