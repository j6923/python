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
    strike = 0
    ball = 0

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
#못세우는 건지, 코드를 못 하는건지 #어떤 접근 필요한지 부족 #옮기는 게 안돼는 것은 문법이 부족한것 
#둘 다 안돼면 둘 다 해야 #첫번째 것이 