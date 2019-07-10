import requests
from bs4 import BeautifulSoup

url = 'https://www.bithumb.com/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class': '#tableAsset'})
data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))

    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            real_time_price = tds[1].text
            data.append([point, real_time_price])

data
with open('get_coin_info.csv', 'r') as f:
    get_coins_info = f.readlines()

with open('get_coin_info.csv', 'w') as f:
    f.w('point, real_time_price\n')
    for i in data:

            f.w('{0}, {1}\n'.format(i[0], i[1]))
# https://dojang.io/mod/page/view.php?id=2458 참고