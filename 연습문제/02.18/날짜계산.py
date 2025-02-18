import datetime
days = ['월', '화', '수', '목', '금', '토', '일']
ey, em, ed = map(int, input("수료 날짜를 연도, 월, 일로 적어주세요.").split())
cy, cm, cd = map(int,input("추석 날짜를 연도, 월, 일로 적어주세요.").split())
end = datetime.date(ey, em, ed)
chuseok = datetime.date(cy, cm, cd)
diff = chuseok - end
print("수료 후 추석까지는", diff.days, "일 남았습니다.")
print("추석은 " + days[day.weekday()] + "요일입니다.")