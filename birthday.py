import datetime

days = ['월','화','수','목','금','토','일']
#input 값이 문자열이므로 datetime 함수는 에러 발생함-> split 함수로 으로 정수 변환함
year, month, day = map(int, input("생년월일을 yyyy mm dd 형식으로 입력하세요: ").split())

birthday = datetime.date(year,month,day)
day =datetime.date(year,month,day)
today = datetime.datetime.now().date()


#print("생일:", birthday)

diff =today - birthday
print(f"생일로 부터 {diff.days} 일 지났습니다" )
print("그날은 " + days[day.weekday()] + "요일 입니다.")

