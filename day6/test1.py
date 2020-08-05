
#fuction: 함수 
#반복되는 코드를 줄여주기 위해 특정 코드에 이름을 부여해놓은 것 
#불러서 실행 : 호출(언어에서는 이렇게 말함)
#내장함수: 원래 설치되어있는 것이어서 필요하면 불러서 씀.
#사용자정의함수: 만들어서 정의해서 씀. 
#def 함수명(매게변수, 매게변수, 매게 변수, ...):
#        실행문장
#        실행문장 
#        return 결과값 
#        return안 줄 수도 있음. 

#바꾸거나 변경할 수 있는 변수 : 매게 변수, 항상 여러개 가질 수 있음 
print("1111111111111") 
def double(x): #사용자가 준 값을 x라고 하면 
    print("2222222222222")
    return x*2 #사용자가 뭔 값을 주면 2배하고 
print("3333333333333")

y = double(10) 
print(y)

  #전달할 매게변수에 맞는 값
#10을 받아주는 변수 매게변수 
#이렇게 전달하는 값을 argument 인수 

#11함수에 이런함수있네 def double cnffurgo 3333 실행해 10을 x에 매게변수
#되면서 출력  return 결과값을 날 호출하네 돌려줘 double 지우고 이 거 써줘. 
#변수에 담던 출력해서 바로 쓰던 함. 


k = double(20)
print(k)
print("----------------------------------------------------")
#로또번호 생성기
lotto = []

#1. 랜덤하게 1부터 45 사이의 정수를 생성한다. 
import random 
# lotto = random.randint[range(1,45)]
# for i in lotto:
#     for j in range(6):
#         if lotto 

# random. randint(1,45)\

# lotto.sort()
# print 
# #2. lotto 리스트에 담는다.
# lotto.append(1)
# print(1) 
#3. 중복된 값이 있으면 다시 뽑는다. 
#4. 6자리가 모두 완성되면(들어가면)
#5. 정렬한다. 
#6. 출력한다. 
def getLotto(no): 
    for t in range(no): #안에 있는 부분 3번 반복 하면 됨 
        lotto = []
        i = 0 
        while i<6: #i가 6보다 작으면 다시    (0,1,2,3,4,5) 6번만 하면 되니까 6보다 작음
            j = random. randint(1,45)  #랜덤하게 뽑기 1부터 45까지 
            if j in lotto:              #만약 lotto 가 j면 
                continue #있으면 넘어가 하지마 pass  
            else:                        # 아니면 
                lotto.append(j)           #lotto.append에 포함시켜 릿트에서 똑같은 값이 있으면 컨티뉴 
                i+= 1 #증가시키고 반복     i는 i+1해 
        lotto.sort()
        print(lotto)                      #그리고 출력해 


        print(20 in lotto) #있으면 T 없으면 F in으로 거기 있는 것중에 하나가 맞아?

        #for는 갯수 해줘야 되서 여기서는 while씀,  while은 조건으로 함.  


    #len작잖아 더 돌아, set 해서 할 수도 있음. 
    return lotto 



#getLotto(3) #호출 #3번 나왔으면 좋겠어요. 3번 
#웹브라우저에 띄우고 싶어요. 함수로 만들어져 브라우져로 보내면 댐, 콘솔로 
#리터런트로 만들어주는게 가치가 큼 

getLotto(3) #argument, 인수



    #print(value)
    #return value

#3! #팩토리얼  
# ---> 5*4*3*2*1
# value = 1 
# for i range(5,1,-1):
#     value = value*1
#     print("3! = ", value)

def factorial(n):
    value = 1
    for i in range(n,1,-1):
        value = value*i
        print(str(n) + "! = ", value)
        return value
x = factorial(3)
y = factorial(5)

print("x :", x, "y: ", "x + y", x + y )

print("--------------------------------------------------")

#반환값이 있는 함수와 반환값이 없는 함수로 나눌 수있음.

#5*4*3*2*1 =120 형식으로 출력하는 factorial2() 함수를 정의하세요 
def factorial2(n):
    '''#혹은 더블코테이션 3개 
    이 함수는 내가 그냥 심심해 만들어본거니 쓰라믄 쓰고 ^^ 
    얘는 뭐하는 겁니다, 다큐먼트 주석, 쓰는 사람이 간단하게 쓸 목적으로
    만든 것임.  #얘도 들여써야함. 
    # :만나면 무조건 들여써야 함 
    '''
    value = 1 
    for i in range(n,0,-1):
        value = value *i 
        if i >= 2: 
            print(i, " * ",end=" ") 
        else:
            print(i, " = ", end=" ")
    print(value)
    
factorial2(7)

print(factorial2.__doc__) #underbar, underbar 2개 
#쓰는 사람은 함수 이름과 doc뭐라고 되는지 보고 사용하는 것. 
    
    #맨 마지막것 안 나왔으면 좋겠어요.     
    
     #5부터 -1로 출력 
print("=======================================")

help(factorial2)  #help(함수명) 써도 됨. 






