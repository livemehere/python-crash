import requests
import json
from bs4 import BeautifulSoup
import mongo

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
movies = soup.select('#old_content > table > tbody > tr')

db = mongo.get_database()

for movie in movies:
    a = movie.select_one('a')
    img = movie.select_one('.ac > img')
    point = movie.select_one('.point')
    if a is not None:
        title = a.text
        rate = img['alt']
        point = point.text
        obj = {'rate':rate,'title':title,'point':point}
        db['movies'].insert_one(obj)

