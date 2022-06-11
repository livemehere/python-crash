from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
html = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')

rows = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for row in rows:
    rank = row.select_one('td.number').text[0:2].strip()
    title = row.select_one('td.info > a.title.ellipsis').text.strip()
    singer = row.select_one('td.info > a.artist.ellipsis').text
    print(rank,title,singer)