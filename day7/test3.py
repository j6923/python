#함수 map : bilt-in함수 기본적으로 들어가 있는 함수: print, input, random :list나 dictionary와 같은 iterable 한 데이터를 인자로 받아 
#list 안에 개별 item을 함수의 인자로 전달하여 결과를 list형태로 주는 함수 

def func1(x):
    return x*2
#간단한 로직이란 뜻에서 이렇게 함. 
n=[]
m = [10,20,30,40] 
for i in range(len(m)):
    n.append(func1(m[i]))
# m = [10,20,30,40] #집어넣으면 10꺼내서 놓음, 20이 되서 돌아옴. 
for i in range(len(m)):
    n.append(func1(m[1])) #1번의 매게변수, 다른 리스트에 넣고  
print(m) #[20,30,60,80 ] #map함수 하면 쉽게 됨

print(list(map(func1,m ))) # 리스트로 형변환 시켜주고 싶어요. 

t = {1:100 ,2: 200, 3: 300} #딕션어리---- 키 : 밸류

# print(list(map(func1,t))) #키는 접근가능 , 그냥 쓰면 다 키, func1 , 두배니까 [2,4,6] , 키가 아닌 밸류넣고 싶어요. 리스트로 넣으려고요 

print(list(map(func1,[t[i] for i in t]))) #2에 전달, 3에 전달, 4에 전달 #t랑 벨류 t[i]


print("---------------------------------------------------------")
for i in t:
    print(i) #t[키] >>>>>>  value값 나옴 

#리스트나 딕션어리같은 잘 변하지 않는 immunable 맵함수 이용 적용한 애들 가지고 와서 리스트형변환 가능 
# 
# 
a = [1,2,3,4,5,6,7,8,9,10] 

#3의 배수만 출력 





#makeString(x) --- 숫자를 넣으면 문자로 바꿔서 줌 
print([str(i) for i in a if i%3==0]) #a에서 꺼낸 a,a값이 3을 떨어진 아이만 가지고 옴  #3의 배수

#숫자로 넣으면 문자로 바꿔서 나오게 함. 
def makeString(x):
    return str(x)
#map함수 이용해서 하기 
# print(map(함수명, a))
print(list(map(makeString, a))) 
#3의 배수는 문자, 나머지 숫자 
def makeString(x):
    if x%3==0:
        return str(x)
    else:
        return x 

#람다식으로 
print(list(map(lambda x : str(x) if x%3 == 0 else x, a ))) #makingstring을 람다식으로 위의 것을  #lambda에서 x는 매게변수 if x%3만족하면 str(X) 만족 안 하면 x,그리고 a 값임 
#함수 이름없으니까 이름안씀 매게 변수는 x를 쓰고 있고 리턴 값이 오니까 조건이 들어가요  ,, a하면 다 string a하면 다 글자됨 
#소수 : 1과 자기자신으로 나눠지는 수  
# def primeNumber(x):
#     if x%1==0 or x%x==0 
#         return float()   나 
#     else:
#         return x 

     


#실수로 린턴: float() : 3------> 3.0 
#아니면 자기자신 : 4 ---> 4 
#실수 : float():3 -----> 3.0           
#
# 람다식으로 출력                                                            


#filter : 조건에 일치하는 값만 추출할 때 사용하는 함수 

def test2(x):
    if x>0:
        return x 
    else:
        return None  #함
# 대신에 필터씀 
n= [-3,-2,-1,0,1,2,3]

print(list(filter(test2,n)))  #조건에 만족하는 애들만 꺼내서 list만듬 

#test2를 람다식으로 표현
print(list(filter(lambda x : x>0, n)))

#60이상 
score = [80,70,53,90,70,80,49,99]

# for i in range(9):
#     if score >= 60:
#         return score 
#     if score >= 70 and score <=90: 
#         return score 

#print(list(filter())) 

#70점이상 90점 사이 
#filter을 이용해서 하기 


#현재 작업디렉토리에서 파일들의 목록 가져와 

file_names = ['movie1.jpg', 'movie2.png', "rabbit.png","bg.png", 'test.txt', 'test2.py']

#png 파일의 확장자만 검사해서 파일의 이름을 선택

['movie2.png', 'rabbit.png', 'bg.png'] ##그런 글자가 없으면 없으면 -1 find, 그런 것만 가지는 것을 find로 찾기 
   #람다함수로 찾기 


print("-----------------------------------------------------")
print("movie2.png".find(".aaa"))

def png_Finder(x): #문자열 주면 
    if x.find(".png") != -1:
        return x 
    else:
        return None 
    
#글자가 있어 없어? 없으면 none 
        # print("없네")

png_Finder("movie2.jpg")

#람다식으로 바꾸기 
# ['movie2.png','rabbit.png','bg.png']
print("movie2.png".find("aaa"))
print(list(filter(png_Finder,file_names))) #리스트로 만들고 그것을 출력해요  뒤에 함수 적용해서 가져옴, 필더 만족 하면 가져오고 아니면 버림 

#함수 있으니까 쓰면 되지만 람다식으로 쓸 수 있어써요, 람다식으로 어떻게 쓸가요 ? def 대신에 람다, 함수이름 안써 , x.find -1이 있어 조건식 
print(list(filter(lambda x: x.find(".png")!= -1, file_names)))