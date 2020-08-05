a = (10, 20, 30, 40, 50)

print(a)

#지금은 소괄호 아까는 대괄호 
#이렇게 하면 이름이 달라짐, 이런대을 --> '튜플'이라고 함 
#값이 나열되어 있음 요소가지고 있고 

b = tuple(range(5, 10)) #이렇게 쓸 수 있음 
print(b)
#list 비슷하지만 한 번 생성디면 값을 변경할 수 없다. 
#그래서 불변한 순서가 있는 객체의 집합을 튜플이라고 함 
print(a[0]) # 0번 1번 할 수 있음 레인지 해서 
#print(b[2]) = 100 이렇게 쓰면 변경불가하다고 에러남, 왜냐면 튜플#숫자 변경 
#실수로라도 변경되는 것 방지가능
#조작하느라고 할 수있음, 읽기 전용하고싶어
# 길이를 알고 싶어요 len() 몇 칸인지 알고 싶어 
print(len(a)) 



#제어문: 문장의 흐름을 제어해주는 명령어
#일반저그올 인터프린터여서 한 줄 한 줄 읽음 
#특정한 부분 이동시킬 수 있는 문장 
#반복하고 싶어요 : for
#for 변수 in 자료형(iterable) 
#    반복할 명령

for i in a: 
    print(i) #프린트여서 아래로 내려감. 아무 변수나 상관없음 꼭 i아님 
#a에 있는 값에서 꺼내서 i에 담음, 그리고 출력 그것을 
# 다시 위로 돌아가서 반복함, 그래서반복문, list나 튜플도 올 수 있음. 
    #콜론드로 끝나고 들여써서 코드블럭이라고 표현  
print("test................................")
#반복하고 나서 한번만 출력  #빠져나와 얘를 출력하고 종료 


#1부터 20까지 화면에 출력 
#1.프린트문으로 출력
#2. for문 코드를 간결하게 줄이기 
print(list(range(1,21)))
b= (list(range(1,21)))
for i in b:
    print(i)
print("test2-------------------------------")
#수업
k = list(range(1,21))
print(k)
for j in k:
    print(j)
# 반복문 사용해서 구구단 3단 출력 
k = list(range(1,9))
print("3*1=3")
print("3*2=6")
print("3*3=9")
print("3*4=12")
print("3*5=15")
print("3*6=18")
print("3*7=21")
print("3*8=24")
print("3*9=27")

#변하는 부분 변수로 
#su = 1
#print("3*" + str(su)+str(3*su))
#su = su+1
#print("3*" + str(su)+str(3*su))
#su = su+1
#print("3*" + str(su)+str(3*su))
#print("3*" + str(su)+str(3*su))
#print("3*" + str(su)+str(3*su))
#print("3*" + str(su)+str(3*su))
#print("3*" + str(su)+str(3*su))
#print("3*" + str(su)+str(3*su))
#print("3*" + str(su)+str(3*su))

#반복할 거예요
c = list(range(1,10)) 
for su in c:
    print("3*" + str(su) + "= " + str(3*su))

#1부터 10까지 합을 누적합을 출력 
#1. 1부터 10까지 값을 화면에 출력한다. 
#2. 누적합을 담을 변수를 선언한다. 
#3. 출력하기전에 변수에 진행값을 담는다 
#4. 누적값을 출력한다.


#나 
d = list(range(1,11))
for i in d:
    print(i) #i하면 1...10 출력 



sum = 0 # 빈통 
for i in (range(1,11)): 
    sum = sum+i 
    print("sum :", sum , "i :",i)
#print("sum :", sum , "i :",i)
 #퐁 넣어도 됨  리스트니까 1씩 꺼내 쓰니까 리스트 필요 없음 
 #하나의 덩어리 --- 들여쓰기 하면
print("-----------------------------------------------")
#1-100까지 누적값 계산 
sum2 = 0 #재활용해도 됨 변수명 
for i in range(1,100):
    sum2 = sum+i
    #print("i :", i, "sum2 :", sum2)
print("1부터 100까지 누적합 :" , sum2) #밖에서 실행 




#sum2 = 0
#for i in input("1부터 100까지를 입력하세요"):
    #sum2 = sum+i
    #print("sum2:", sum, "i:" i)


cnt = input("누적합 수를 입력하세요")
cnt = int(cnt)+1
sum2 = 0
for i in range(1, cnt):
    sum2 = sum2+i
print("1부터", cnt-1, "까지 누적합 :" , sum2)



#입력받는 구구단 출력 
# 몇 단? 3
#입력 구구단 3단 출력 
d = list(range(1,10))
sum3 = 0
for su in c:
    print("3*"+str(su) + "= "+ str(3*su))
#for su in c:
    #print("3*",su,"=", 3*su)

print("====구구단------------------")
dan = int(input("몇단 : "))
#print(dan*100)
#range 0생략 가능 하나만 10이면 0~9까지 
value = 0 
for i in range(1,10):
    value += i 
    print("test...", i, value) 

    #i값이 얼마인지 알면 알 수 있으면 좋겠음  
  #ctrl f5  value 
#숫자니까 곱해진 값 볼 수 있음 

#숫자, 예약어 X for 문 등 함수 등을 예약어라고 함 
#대소문자 구분합니다. 
#의미있게 짓기 
#영어 
#
    


