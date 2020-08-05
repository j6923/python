
#가위 바위 보
print("1. 가위 2. 바위 3. 보")
userinput = int(input("가위 바위 보 중 선택하세요: ")) #사용자에게 입력받음 가위가 같으면 사용자 가격은 1,2,3 if문으로 하면 됨   
#가위 바위 보라는 글짜를 가진 리스트를 선언 
#0,1,2, 중 한 개를 리턴하는 랜덤인트 함수를 사용하여 뽑음
#출력 : 리스트[x]

userInput = 1 #사용자가 1냄  #함수 I여야 함. 소문자가 아니라 

import random #random함수 불러냄 
li = ['가위', '바위', '보'] #숫자가 처리하기 제일 편함
idx = random.randint(0,2) #램덤한 정수값을 반환해주는 함수 램덤값 주는 범위 
print(idx, li[idx])

#승부 판정
#userInput <= 0
#램덤  <= 1
#사용자의 입력값과 컴퓨터의 램덤 값의 차를 비교 , 
print("사용자입력값", userInput, li[userInput])   
print("컴퓨터랜덤값", idx, li[idx])
print("차이값", userInput-idx)

#차이값 : 0 이러면 | 비김   #리스트의 값이 0,1,2이기 때문에 차이하면 이렇게 됨.  
dif = userInput-idx
if dif == 0:
    print("비김")
elif dif == 1 or dif == -2:
    print("사용자승")
elif dif == -1 or dif == 2:
    print("컴퓨터승")
#1이거나 -2이면 | 사용자승
#-1 이거나 2이면 | 컴퓨터 승 


#이중 포문 4면 출력 