#csv 파일 ?? -- comma 세퍼레이드 value  
a, b, c = input ("숫자 3개를 콤마로 구분해서 입력하세요: ").split(",") #3조각으로 쪼개, split , ,기준으로 나눠 

print("a :", a, "b : ", b, "c :" , c)

#출력해 주는 함수 enter기능 들어가 있음 : print 

#print(a)
#print(b)
#print(c)

print(100, 200, 300, sep = ", ") # , 로 기준으로 출력해 

print("Hello", "Python", "world", sep="/n") #이렇게 치는 것은 enter야 약속 "/n"
#특수문자 엔터 : 타자기 입력방식 컴퓨터로 가져온 것이 컴퓨터 *캐리지 리턴: 옆으로 보냄 *라이피던: 한줄 위로 보냄
print("아/n 날씨가 /n좋다, /n/t/t/t 놀러/t가야지.. ㅠㅠ")  
#특수문자, 제어문자라고 함 : /n -->enter    /t: tab
print("오늘은") #오늘은 /n 끝날때는 enter야 print함수 


print("오늘은") #enter 대신 tab 
print("수요일")
print("내일은")
print("목요일")


print("목요일", end="/t")


#오늘은 수요일, 내일은        목요일 
print("오늘은\n 수요일","내일은 \t\t\t 목요일",sep=',')


#year, month, day, hour, minute, second 변수를 선언하고 
#값을 대입한 후에 
#아래와 같은 출력을 얻도록 코드를 작성해 보세요. 

#오늘은 2020./7/15 18:00:00
year=2020
month=7
day=15
hour= 18
second = 25
minute = 30
print("오늘은"+str(year)+"/"+str(month)+'/'+str(day), ""+ str(hour)+":"+str(minute)+":"+str(second)+"입니다")

print(year, month, day, sep="/", end=" ")
print(hour, minute, second, sep=":")
#print(year, month, day,??????)
#18:00:00
#print(hour, minute, second, ?????)




