

#1부터 100까지 수 중 3의 배수 5개만 출력 


#3의 배수 왕창 출력(모르겠으면)

tot = 0
for i in range(1,101):   #하다가 이 조건 만족하면 break하면서 더 이상 반복 안 함. 
    if i%3 == 0:          #반복하는 횟수 줄어듬,
        tot+=1
        print(i)
        if tot == 5:
            break


for i in range(1,101):
    if i%3 == 0 and tot <5:
        tot+=1   # 오래걸#반복 100번 다 검사함. 
        
    
            