days = ['월','화','수','목','금','토','일']
day1 = datetime.date(2025,2,18)
day2 = datetime.date(2025,5,5)
diff = day2 - day1
print("어린이 날까지 남은 기간:", diff.days, "일")
print("그날은" + days[day2.weekday()] + "요일 입니다.")

days = ['월','화','수','목','금','토','일']
day1 = datetime.date(2025,2,18)
day2 = datetime.date(2025,5,8)
diff = day2 - day1
print("어버이 날까지 남은 기간:", diff.days, "일")
print("그날은" + days[day2.weekday()] + "요일 입니다.")

days = ['월','화','수','목','금','토','일']
day1 = datetime.date(2025,2,18)
day2 = datetime.date(2025,12,25)
diff = day2 - day1
print("크리스마스 날까지 남은 기간:", diff.days, "일")
print("그날은" + days[day2.weekday()] + "요일 입니다.")