import time #시간과 관련있는 모듈 

# #모듈에 대한 설명 나옴, 실행=== q로나옴 

help(time.time) #floating point number   #1970년 c언어 부터 시작 날짜를 표기해야 겠는데 기점 1970년 1월 1일로 하지 뭐. 기점을 거의 거기로 삼음.  

#초단위를 return하는 함수 ....초단위로 현재시간을 리턴


print(time.time())


#그래서 ctime 만듦
print(time.ctime(),type(time.ctime()))

#연도 4자리찍어보기  str문자열 이래요.
# 자르면 리스트 얻어오기 끝에 있는 거 하나만 얻어오면 되겠다. 
time.ctime().split() #공백단위로 끊기 
print(time.ctime().split()[4]) #split으로 공백을 나누고 4번째 자른다. 
print(time.ctime().split()[-1]) #split으로 공백을 나누고 뒤에서 1번째 자른다. 

#지금 시간을 1초에 한번씩 출력 
for i in range(100):     
    print(time.ctime())  #출력 100번하게됨. 

#1초만 자 
# while True: #1초에 한번씩
#     time.sleep(1) #1초 잠들어라.. 
#     print(time.ctime())


print(dir(time)) #time이란 모듈에 어떤 항목이 있는지 볼 수 있음 
#local 현재 로컬 시간 gmtime -- gmt 시간 get clock info -- 시계나오는 것 

    