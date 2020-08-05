import random 
#누군가가 만들어놓은 게 있어요, 내장된 함수, 그리고 다른 사람들이 만들어 놓은 함수가 있어요, 그것을 import라고 해요. 
#기능이 필요할 때만 불러다 쓰는 것. 

for i in range(10):
    print(random.random()) # 0~1사이의 실수 값 
     

 #값을 모르니까 10번 볼려볼게요.

 #random하게 정수 돌려줄수  있음 이렇게 하면 random하게 정수 돌려줌
for j in range(100):
    print(random.randint(1,6))   #randint 안의 있는 숫자 램덤하게 정수 나오게 해줘  


#램덤함수 끝 

#----------------------------------------------------------------
#
cnt = int(input("몇 번 : "))  #여러번 출력하고 싶어요. shift tab(나중)  #프로그램 몇 번 돌리까, 몇 번으로 for문을 돌릴거예요. 
for k  in range(cnt): # for문에 한 번  밑에 
    
    m = list(range(1,46))   #순서가 있고 중복된 값도 가질 수 있다. 
    #1부터 46까지 1`45나옴 m에 저장 

    #print(m)

    #m 리스트의 요소 중 1개를 램덤하게 두 개의 값을 출력하고 싶음
    a = random.randint(0,44)  #a와 b는 0-44안에 있는 정수형 1반환, 리스트에 있는 정수 하나를 보겠다, 그래서 ,a b 만듦 m에는 0-45 총 45
    #print(m[12])
    #print(m[random.randint(0,44)]) 같이 한번에 사용가능 
    #0부터 44사이 정수구하고 

    #두 개 쓰고 싶어요. 

    a = random.randint(0,44)
    b = random.randint(0,44)
    #print("m[" , a, "] : ", m[a], ", [", b, "]) : " , m[b]) #이것은 보기 좋게하기 위해서 
    m[a], m[b] = m[b], m[a]
    #print("m[" , a, "] : ", m[a], ", [", b, "]) : " , m[b])

    #여러번 시킬 거예요. 
    for i in range(1000): #숫자 바뀐 것을 1000번 함, 전체적으로 섞이게 됨. 
        a = random.randint(0,44) 
        b = random. randint(0,44)
    #print("m[" , a, "] : ", m[a], ", [", b, "]) : " , m[b]) #이것은 보기 좋게하기 위해서 
        m[a], m[b] = m[b], m[a]
    #print("m[" , a, "] : ", m[a], ", [", b, "]) : " , m[b])

   # for j in range(6):
        #print(m[j], end = "\t")    #정렬해서 출력 

    #1. 새로운 리스트 6칸자리 만들고 
    #2. 앞에서 6개 새로운 리스트 담기 

    #3. 6칸짜리 리스트를 정렬 
    #4. 순서대로 출력 
   # for j in range(6):
        #print(m[j], end = "\t")   
        

        #1. 새로운 리스트 6칸자리 만들고 
    #f = list(range(0,45))
    #2. 앞에서 6개 새로운 리스트 담기 

    #3. 6칸짜리 리스트를 정렬 

    #4. 순서대로 출력 
            
    n = list(range(6)) #list 비어있는 것 하나 만들고 돌림. 
    #print(n)   #6개 담을 리스트를 만듦. 


    for j in range(6): #6개짜리에 5번째까지 출력하면 섞여있어서 
        n[j] = m[j]    #n에 담김, n는 순서로 담아도 정렬 
        #m에 있는 것을 n으로 바꿈. 

   # print(n)
    n. sort()
    #print(n)
    print("----------------------------대박 번호------------------------------")
    for i in range(6):
        print(n[i], end = "\t")
    print()


#여러번 돌리고 싶어요. 
