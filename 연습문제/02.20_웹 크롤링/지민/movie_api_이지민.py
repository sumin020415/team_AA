import requests
import json


key = '02786891f8d65d02591fb254f86dc017'
url =f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt=20250201"


res = requests.get(url)
d = res.json()  

box_office = d['boxOfficeResult']
print(f"박스오피스 유형: {box_office['boxofficeType']}")
print(f"조회 기간: {box_office['showRange']}")

         
print("\n 일별 박스오피스 순위")
for movie in box_office['dailyBoxOfficeList']:
    print(f"{movie['rank']}위 {movie['movieNm']}")

        