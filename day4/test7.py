#쥐띠 
#태어난 연도를 입력하면 어떤 띠인지를 출력 
#자  축  인  묘  진  사  오 미 신 유 술 해 
#쥐 소   호  토  용  뱀  말 양 원 닭 개 돼 
#태어난 년도를 4자리로 입력 : 2020 
#당신의 쥐띠 입니다.  #3으로 나누면 3의 배수인지알 수 있어. 년도를 12로 나눈 나머지 
#4 5 6 7 8 9 10 11 0 1 2 3 print(2020%12) 
year = int(input("태어난 년도를 4자리로 입력:"))
year %= 12
print(year) 
if year == 4:
    print("쥐띠")
elif year == 5:
    print("소띠")
elif year == 6:
    print("호랑이띠")
elif year == 7:
    print("토끼띠") 
elif year == 8:
    print("용띠") 
elif year == 9:
    print("뱀띠") 
elif year == 0:
    print("원숭이띠") 
elif year == 1:
    print("닭띠") 
elif year == 2:
    print("개띠") 
elif year == 3:
    print("돼지띠") 
