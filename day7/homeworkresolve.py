##1. 복구화함수 쓰기 
# def 함수명(매개변수, 매개변수): 
#     코드불럭
#     코드블럭

def setEncryption(msg):
    v = "" 
    #msg의 문자열에서 한 글자씩 
    #ASCII 구한다. 
   # 구한코드 값에 +3
    #이 값을 문자열로 변환
    #string으로 린턴하는 함수쓰기 
    for i in range(len(msg)):    
    # print(ord(msg[i]]) #msg[i]data의 i번째하면 글자 한 자씩 가능 값을 담아놓고 쓸 수 있음  
    #내가 구한 글자에 3을 더해서 구함 
        code = ord(msg[i]) 
        code +=3
        if code >= 91 and code <=93:      #x가 88이니까, 88,8990, 3더하는 것 값이 이것보다 작으면 대문자면 23차이있음#앞에 있는 것 or 뒤의 조건 할 수 있음 
            code -=26                           
        elif code >=123 and code <= 125:    #소문자일 수 있음
            code-= 26  
        # print(chr(code))   중간과정 출력과정보려고 함. 
        # print(msg) 
        v += chr(code)
    # print(v)
    return v
# setEncrypton("Hello") #인수값이 자동으로 msg에 각인되서 print msg에 출석 
data = "XYZA"  #{|}d됨  #범위가 있다면 앞자로 밀어서 해야함.   # 만약에 알파벳이 x,y, z,면 a,b,c,로 바꿔줘야 함. x, y,z --->a,b,c 
#대문자일 수 있음 대문자로 바꿔줘야 ---> X,Y,Z--> A,B,C 아스키코드를 알아야 함. 
x= setEncryption(data)  #data의 값을 msg에 준 것이기 때문에 data와 msg다를 수 있음.
print(x) 

#복구함수는 이름을 getDecode
def getDecode(msg):
    # pass
    v = ""
    for i in range(len(msg)): #길이만큼해야 2개면 2개만큼이 나옴, 다 나오게 반복하게 하기 위해서 
        # print(msg[i]):#
        #ascii code 로 만듦
        code = ord(msg[i]) #한글자 한글자 아스키코드 구함
        code -=3
        # v +=chr(code) #내가 준 길이만큼을 구하고 아스키코드를 구하고 하나씩 붙임, 중간과정 
        # print(chr(code)) 중간 과정 
        if 62 <= code  <= 64: #알파벳의 범위 넘어서는 것을 범위 넘어서지 않게 조정. 
        #code >= 62 and code <=64: 이렇게 쓰는 게 낫지만 왼쪽도 지원하기는 함.       
            code += 26
        elif 93 <= code <= 96: #소문자라면
            code += 26
        v += chr(code)  
        #print(v)
    return v 
print("=================================================")

#a, b = b, a 일반적 프로그램언어는 지원안함 
y = getDecode("ABCD")  #이 값을 주게 함
print(y) 

# for i in s:
#     print(ord(i)+3) #한글자 한글자 출력 
# m = ord(i)-3
# print(chr(m))

#값을 대입하는순간 문자이든 숫자이든 상관없이 자료형 결정됨, 값을 닿는 순간 그 값으로 결정  
#v문자는 문자인데 비어있는 문자 v="" 글자 한글자씩 넣을려고 ---앞에 v = "" 이유  



#3. 야구게임 
import random 
com =[]
cnt = 0
while len(com) < 3:   #3자리뽑음 
# for i in range(3): #3번 반복할수 있음 
    rnd = random.randint(0,9) #세자리 정수를 얻을 수 있음101~999. 리스트에 각각 넣어서 100의 자리, 10의 자리 할 수도 있음 #random.randint(0,9)
    if rnd in com: #여기에 있어 
        continue #그럼 패스 
    else:    #그렇지 않으면 
        com.append(rnd)
print(com) 

#사용자로부터 3자리수를 입력받는다. 
while True:
    cnt += 1
    userData = int(input("3자리 숫자를 입력하세요")) #356 
    user =[]
    user.append(userData//100)
    user.append(userData%100//10) #100으로 나눈 나머지를 다시 10으로 나눔
    user.append(userData%10)
    print(user)
# user[0] = userData//100
# user[1] = userData%100//10 #100으로 나눈 나머지를 다시 10으로 나눔
# user[2] = userData%10 

# 
#3. 판별한다. 
# if com[0] = user[0]: #user의 0번째와 같아요? 
#     strike+=1 #같으면 strike 변수에 1을 더해요. 
# if com[1] = user[1]: #user의 0번째와 같아요? 
#     strike+=1 #같으면 strike 변수에 1을 더해요. 
# if com[2] = user[2]: #user의 0번째와 같아요? 
#     strike+=1 #같으면 strike 변수에 1을 더해요. 
#풀어쓰면 

 

#for문으로 줄여보기 

    for i in range(3):                               
        if com[i] == user[i]:     #i가 1번 user의 10의 자리가 같아요 아니요 j  9와 3은 같지 않아요, 같으면 볼 10의 자리 일치해? 비교해서 같은게 있으면 볼 
            strkie+=1
        else:
            for j in range(3):
                if com[i] == user[j]:
                    ball+=1 #판별한다. 


    print(str(strike)+"S", str(ball) + "B")   #if문으로 쭉 늘어놔도 할 수 있어요. 


    if strike ==3:
        print("짝짝짝 축하합니다..")
        break #3스트라이크면 break 

#cnt 몇 번만에 출력했어요. 
#나는 어떤 과정으로 풀어갈거야 세울 수 있어야 함. --- 알고리즘. 한글로라도 쓸 수 있음, 안돼면 절대 프로그램 못 씀. 
#못세우는 건지, 코드를 못 하는건지 #못 세우는 것은 어떤 접근 필요한지 부족한 것임 #옮기는 게 안돼는 것은 문법이 부족한것 
#둘 다 안돼면 둘 다 해야 #첫번째 것이 