import requests
import bs4

url = 'https://naver.com/'
selector = '.ah_k'


html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')

ranks = soup.select(selector)

for rank in ranks:
    print(rank.text) #.text는 text만 가져오는 것
