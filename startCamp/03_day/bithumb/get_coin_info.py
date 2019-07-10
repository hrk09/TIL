# 1. html 사이트 가져오기(bitthumb 페이지)
import requests
import bs4 # import 문은 파일 최상단에 올린다.
import csv

response = requests.get('https://www.bithumb.com/') 
# 요청을 보내 응답을 받는다.
html = response.text
# 응답받은 객체에서 html 문서를 string으로 가져옴

# 2. beautiful soup 모듈 이용하여 string 타입의 html을 파싱한다.
soup = bs4.BeautifulSoup(html, 'html.parser')

# 3. 각 코인의 정보가 담겨있는 table row 데이터를 list 의 형태로 가져온다.
coins = soup.select('.coin_list tr') 
# coin_list 안에 있는 tr 태그에 접근한다.(띄어쓰기)

# 5. csv writer를 이용해 정보를 저장한다.

with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)

# 4. 각 코인을 순회하며 필요한 정보만 추출한다.
    for coin in coins:# coins는 tr의 리스트
        # 각 코인의 이름과 시세 데이터를 추출(한 줄의 데이터 안에는 이름과 시세 有)
        coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text
        #.text.replace('NEW', '')도 가능 
        # td 안에 p 태그 안에 a 태그 안에 strong 태그
        coin_name = coin_name.replace('NEW', '').strip()
        coin_price = coin.select_one('td:nth-child(2) > strong').text
        data = (coin_name, coin_price)
        csv_writer.writerow(data)
        print(data)


