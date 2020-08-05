
    
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
