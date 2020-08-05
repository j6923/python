#time converter
#Wlrdmaus 시간이 입력되고 
#1일 1시간 1분 1초 입니다. 나옴 
time = int(input("시간입력:"))

print(time)

#1분 ===> 60초
#1시간  ---> 60*60초 
#1일 ---> 60*60*24  #코드는 가독성 있게 써주는 것이 좋아 

day = time/(60*60*24)   # 5000
time/(60*60*24)   #혹시 연산자 우선순위 흐트러질까봐 괄호 씀   1시간 3600초
hour = time%(60*60*24)/(60*60)   #86400   1일 
minute = time%(60*60)/60  #hour #time%(60*60*24)%(60) 
second = time%60
# 5000/86400--- 몫 : 일 

print("%d일 %d시간 %d분 %d초"%(day, hour, minute, second))

# 3661 

# 11번 
