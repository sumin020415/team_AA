#사이트의 1페이지 기준으로 작성 하였음

import requests as req
from bs4 import BeautifulSoup as bs
url ="https://finance.naver.com/sise/sise_market_sum.naver"
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
#*mobile 받아오면 모바일 화면을 그대로 받아올 수 있으므로 pc와 다름 주의 
web = req.get(url , headers = headers)
a= bs(web.content, 'html.parser')          #bs 라이브러리를 이용해 html 파싱



item = a.select('.tltle')                  #클래스 =. tltle의 요소(종목)들을 가져옴 

won = [element.get_text(strip=True) for element in a.select('.number')] 
#number클래스에 현재가 목록을 리스트로 받아온다. replace함수가 생각나겠지만, 문자열에서만 써야함으로 리스트에서는 사용 할 수없다. 
#가격의 리스트를 순회 하면서 element에 하나씩 저장하고, get_text()로 html 태그 안의 텍스트만 추출 한다. , strip = true 옵션은 앞 뒤 공백과 줄바꿈을 자동으로 제거한다. 



#print(len(won))                            #현재가의 리스트 길이 알아봄 1페이지 기준 50개
now_won = [won[i] for i in range(0, 500, 10)] 
#number 클래스에 종목만 뜨는게 아니라 전일비, 등락률,액면가, 시가총액 ... 순으로 9개의 클래스가 더 존재함 -> 한 종목 당 총 10개의 클래스가 존재함 -> 여기서 제일 상위의 인덱스가 가격이다. 0,10,20,30... 만 받아 와야 가격만 받아 올 수있음.    for문을 써서 500개의 스크립트 내에서 10개씩 증감 해줘서 50개의 가격을 출력한다.
#print(now_won)                            #가격들의 리스트들(50개)


print(f' {"종목명":<10}{"현재가":>6}')
print('-' * 25)
for bb,ww in zip(item,now_won):
     print(f'{bb.text}: {ww}원')
    
   

