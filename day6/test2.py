
def add(a,b) :
    '''
        두수의 합을 리턴합니다. 
    ''' 
    #c = a+b 
    return a+b #위의 것 c로 써도 되지만  #변수 선언할 필요없으면 더해진 값 리턴하면 됨. 
def minus(a,b):
    '''
     두수의 차를 리턴합니다.
    '''
    return a-b
x = add(100, 200) #300 add니까 플러스 
y = minus(200, 100) #100 minus니까 마이너스 



print(x + y) #400 #300+100이니까 

help(add) # 두수의 합을 리턴합니다. 
help(minus)# 두수의 차를 리턴합니다. 

#리턴 값 줄 수도 있고 알 줄 수도 있음
#두 개 이상도 가능 
 
def add_minus(a,b):
    return a+b, a-b #뭔지는 모르지만 

x, y = add_minus(300,100) #
print("x :", x, "y :" ,y)

i,j =(1,2) # 튜플을 하나씩 대입할 수 있음. 
#packing묶어놓은 것을 푼다 unpacking 동시에 두개 값 갖음 
i, j =1,2 #괄호 안 써도 튜플, 괄호 생략가능 그래서 위와 같음 

i,j = [1,2] #리스트도 언 팩인 할 수 있음 
#여러개 한번에 받아줄 수 있음. 

#함수에 리턴 값 : 정수, 문자, 실수, 튜플, 리스트도 가능하고 등등등등 


# sumValue = hap(100,200) #합계를 리턴합니다... : 300 

def hap(a,b): 
    return a+b #
sumValue = hap(100,200)
print(sumValue)

#인수의 갯수로 구분함. 
# def hap(a, *b):
#     print("a : ", a)
#     print("b :", b)  에러남 
#     #합계를 구해서 리턴 
    #??? 

# hap(100,200) #합계를 린턴합니다... : 300 

# hap(100, 200, 300)  함수 정해져 있지 않아 에러남 
    
#sumValue = hap(100,200)
#sumValue = hap(100,200,300) 구분이 안됨 

#sumValue = 

#어떤 타입으로 
#튜플로 간주해서 받아버림 

#정수랑 튜플 바로 계산 못함
#튜플하나씩 꺼내서 정수랑 계산하면 됨. 
# def hap(a, *b): #*b: 가변인수 
#     print("a :", a)
#     print("b :", b)
#     v=a #a변수에 값을 v변수에 대입해라 
#     for k in (100, 200):     #자료형 튜플, 앞의 것 꺼내서 담고 앞의 것 꺼내서 다목 
#         v +=k
#         print(k)


# print(hap(100,200))
# print(hap(100,200,300))
# print(v)


def hap(a, *b): #*b: 가변인수   #수가 안 맞아서 가변인수 씀 
    print("a :", a)
    print("b :", b)
    v=a
    for k in b:
             #자료형 튜플, 앞의 것 꺼내서 담고 앞의 것 꺼내서 담어
        v +=k  #v = v+k 
        print(v)

#정수랑 튜플 바로 계산 못하니까 튜플하나씩 꺼내서 정수랑 계산 
print(hap(100,200))
print(hap(100,200,300))

#b는 튜플이니까 하나씩 꺼내서 누적시키는 것 
#여러개 매게변수 갖는 애를 '가변인수'라고 함. 인수갯수가 가변적이기 때문에 
