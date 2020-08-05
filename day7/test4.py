#내장함수-- bilit in fucton
# 
print(sum([10,20,30]), sum((10,20)),sum({2,3})) #리스트나 이런 애들도 가능해요.
#리스트를 매게변수로 갖는 함수(앞), 

print(bin(8)) #2진수 
print(int(2.7), float(3), str(5)+'오') #숫자랑 문자를 더해서 붙일 수도 있음 

a = 10
b = eval('a + 5')
#b = a + 5

print(b) #결과값은 15

 #이 식을 실제 실행시켜주는 함수 #글자를 식으로 시켜주는 함수 a+5라는 식으로 바꿔줌. 
#python java하고 비슷한 것 많음 
print(round(1,2), round(1,6)) # 반올림

import math #수학할 때 함수들이 모듈을 불러오는 것, 함수정의하면 남이 한 것 갖고 올건데,  서로 모아놓은 함수들의 모음

print(math.ceil(1.2),math.ceil(1.6)) #정수 근사치중 큰수, 비슷하지만 큰수 ,,큰 애들중에 제일 작은값  ---> 2나옴  
#이거하고 근사한 큰 수 
print(math.floor(1.2), math.floor(1.6) )          #제일가까운 정수 이값 넘지 않는 가장 가까운 정수  -----> 1나옴 

print("--------------------------------------")
bList = [True, 1, False,0]      

#묶어요, all 
print(all(bList)) #True and 1and False 모두 만족해   
#all 반대는 any 하나라도 만족해? 
print(any(bList)) #True or 1 or False  그 중에 하개라도 만족해 있어? 


#factorial 
# print(factorial(5))
 
 #함수는 다른 함수를 부를 수 있어요. 

def dol():
    print("첫번째 함수실행중")

def do2():
    print("두번째 함수 실행중")

def do3():
    print("세번째 함수 실행중")
    do1() #do1과 do2의 함수를 불러 호출가능 
    do2()
    print("세번째 함수 끝")   #1번불러 1번처리하고 2번불러 2번처리하고 처리하고 끝나요. 

# def sayHello():
#     print("Hello") #sayhello 함수 호출해서 실행 
#     sayHello()#무한루프 sayhello하래요, print찍고 sayhello 실행하고 
# sayHello()#밑에 또 실행하래요
# #재귀적 호출--- 내가 나를 부름. 잘못쓰면 무한 루프 빠질 수 있음. 그만해야 할 조건도 같이 넣어야 그만할 타이밍 잡음. 
cnt = 0  #cnt가 0
def sayHello(cnt):
    
    cnt-=1  #cnt 1중가  #하나씩 감소 
    print("Hello~~~") #sayhello 함수 호출해서 실행 
    if cnt <= 10:
        sayHello(cnt)
    
sayHello(5)
 #cnt 에 5전달 cnt 줄어든 4를 전달 나를 불러, 위에 4할당 cnt3됨 헬로우 찍음 2가 됨, 헬로우 찍음 1이 되고 헬로우 찍고 0보다 큼 0됨, 안 하고 스킵, 종료 
# 팩토리얼 함수 

print('--------------------------------------')
 #120  5팩토리얼 되게 함수 넣어보세요. 
#재귀적 호출을 사용 
def fatorial(n): #fatorial에 n넣음  변수를 줘요.  n에 5넣음 5곱함, 그다음 5*4!값 해도 됨 
    if n==1:
        return 1
    return n*fatorial(n-1) #5를 주면 팩토리얼 4, 4*3*2*1이렇게 됨, 1이면 0팩토리얼 나옴, 그러면 안됨 그래서 if 로 n이 1이니, 그러면 너는 1이야 
#코드는 간결해짐. 

print(fatorial(5))  
#1아님 5* 1이야 주면 이것도 리턴 위에로 리턴 4로 리턴해서 5리턴해서 같이 해줌 ,, 마치 컴퓨터 창이 열리는 것처럼.... 데이터 너무 많으면 일 처리하다말고 그다음 그다음 데이터 많으면 그렇게됨
#재귀적 호출 처리하는메모리상태는 그리 좋지는 않음. 



#피보나치수열을 구하고 싶어요. 
#1 2 3 4 5 6... 숫자의 규칙성 보면 알 수 있음 #수열이라고 했음.  
#1 1 2 3 5 8 13 21.. 1+1은 2 2더하기 1은 3 수열을 피보나치수열 

#fibonachhi(5) #출력되게 하고 싶어요. 이렇게 
def fibonachhi(n): #자연수 만들거니까 n 전체가 있었어요, 전과 전전것의 합이에요. 
    if n<=1: #만약 n이 1보다 작아  1,0
        return n 
    return fibonachchi(n-1)+fibonachchi(n-2) #전값과 그 전값 더한 것 

print(fibonachchi(5)) #for문 돌려서 할 수도 있음.  재귀적 호출사용하면 쉽게 해결할 수도 있음. 
































