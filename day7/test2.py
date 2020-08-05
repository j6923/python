#작은 단위로 하는것이 좋음--- 위의 에러가 밑에 영향을 미치지 않도록 

# mList = [1000,2000,3000,4000,5000] #만원 
#급여 가졌던 값에 10%이상 담으면 됨. 
#for문 사용해서 

# mList2 =[]
# for i in range(len(mList)):
#     mlist2.append(mList[i]*1.1)
    
# for i in range(len(mList)):
#     mList[i] = int(mList[i]*1.1)    방법 1 
#     print(mList) #1100, 2200, 3300, 4400, 5500 

#리스트 내포 표현식 List Comprehension 

# print([int(i*1.1) for i in mList]) #축약형으로 사용가능   #단축표현식 
#리스트 내부에 반복문/조건문의 축
# 약형 형태 전달 가능 

#[리턴값 for i in 대상] 해도 되고 ---- 나오는 값 : 리턴값 
# [리턴값 for i in 대상 if 조건] # 대상에서 꺼내서 i if 조건만족하는 것 리턴해, else는 생략가능 

list2 = [-5, -2, -1,0 ,2, -3, -2, 10, 3]

# #1월 어느날  최고온도 
#영상인 날짜의 온도만 리스트로 작성하려고 한다. 
list3 = []
for i in range(len(list2)): #몇 번째 해서 꺼내오겠다 
    if list2[i] >0 :
        list3.append(list2[i])
    print(list2[i])

list4 = []                 #그냥 값을 꺼내오겠다. 
for i in list2:
    if i > 0:
        list4.append(i)
    print(i)

print(list3)
print("-------------------------------------------------------")
print([i for i in list2 if i > 0]) 
    # print  
# for i in range(9)
print("_________________________________________________________")
#함수 -----> 이름이 없는 함수 "익명함수"라고 함. 메모리를 아끼고,,, 간단하게 하겠다. 
def test(x): #테스트를 람다식으로 표현가능 lambda라고 쓰고 옆 매게변수 씀 콜론 결과만 x+1로 씀, 익명함수처럼 씀. lambda(매게변수): 결과
    


    return x+1

    #함수아니여서 테스트 안씀    

print(test(100))


print((lambda x : x+1)(100)) #실행식 
#특징 : 람다함수(익명함수)
#이름이 없는 함수 
#장점 : 코드가 간결, 메모리의 절약


#왜 절약, def aaa():
#            return 100  #del로 하면 지울 수는 있어요. 제거를 언제가 해야함, 내가... #함수도 객체,그래서 메모리 어딘가에 저장함.  


#가비지콜렉터 garbage collecter #메모리 부족으로 다운되는 일 없어, 파이썬은 ..
    #빨리 다 쓰고 사라졌으면 좋겠어요, 한번 쓰고 끝나는 일회용 ----람다함수 
    #만들었다 사라져 메모리 절약 가능 
    #람다함수 : 정의)이름이 없는 함수, #장점) 코드가 간결, 메모리절약 

def PlusData(a, b):
    return a+b
c = 100
d = 200 
print("before : c :", c, "d: ", d) #두개시켜서 합 바꿔주는 함수 있다고 함. 람다식으로 바꿔보고 싶습니다. 
k = PlusData(c,d)

print(k)


    # 이름없이 람다로 쓰고 싶습니다. 

print((lambda x : x+1)(100)) #실

# lambda a+b : a+b #앞에 람다의 매게 변수 뒤 a+b 

print((lambda a, b : a+b)(100,200)) #괄호 안에 




# print(type(PlusData))
# print("======================================")

# print(k)
# print((lambda a, b: a+b))(100,200) 매게변수가 100하고 200이야 하고 같은 것임. 


print(type(PlusData), id(PlusData))
print('-------------------------------------')

pd = PlusData
print(id(PlusData), id(pd))


print("==========================================================")

lmadd = lambda a, b : a+b  #앞에 이름 
lmadd(1000,2000)  #되듯이 함수가 되므로 매게변수 받음     함수니까 매게 변수 가진거 

print(lmadd(1000,2000))


print("------------------------------------------------------------")
#조건식을 사용한 람다 
# print((lambda a,b: a if a%2==0 else b))   #매게변수 두개 a의 값을 쓰래요 a가 2로 나눈 나머지가 0이면 a 그렇지 않으면 b

#식만 쓴건 괄호하고 두 개 줘야 동작을 함. 
print((lambda a,b: a if a%2==0 else b)(100,31)) 


#




