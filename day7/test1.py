def do_test(x,y): #매개변수 2개 받아 값 출력 실행하고 싶어요, 이렇게 하면 이렇게 실행될 수 있어요 
    print("x :" , x)
    print("y :" , y)
    print("X-Y" , x-y)
    print("sum :", x+y+k)
do_test(100,200) #위치로 값을 전달, x는 100dp y는 200에 값을 전달해서 값을 출력 하나만들어놓고 불러 쓰자. 
#다른 데 만들어놓은 것 불러쓸 수 있음. 
# 값을 전달해서 쓸 수 있음. #바꿔쓰면 x와 y바꾸는 일 생김 
#  어떤 값 넣는냐에 따라 자료형 달라짐 --- 파이썬은 
#순서가 되게 중요할 수 있음 
#무시하고 쓰고 싶어요 

#x =100 , y= 200 z= 200 쓰고 싶어요, 라고 써도 되요, 헷갈릴 때 쓰면 좋음, 
# 전달하는 값 여러개, 갯수 안 맞으면 동작 안됨 ,x,y,k
# 많아도 문제, 적어도 문제   
#여러개 줘도 

# def do_test(*k): #매개변수 2개 받아 값 출력 실행하고 싶어요, 이렇게 하면 이렇게 실행될 수 있어요 
#     print("x :" , x)
#     print("y :" , y)
#     print("X-Y" , x-y)
#     print("sum :", x+y+k)

    #다 받아, x,y 변수는 지금 없으니까 
    #한개 꺼낼 수 있는 로직 있었음 

# def do_test(*k): #매개변수 2개 받아 값 출력 실행하고 싶어요, 이렇게 하면 이렇게 실행될 수 있어요 
#     for i in k:
#         print(i)

#한개 꺼낼 수 있는 로직 ------- for i in k:  

# def do_test(*k): #매개변수 2개 받아 값 출력 실행하고 싶어요, 이렇게 하면 이렇게 실행될 수 있어요 
#     v = 0
#     for i in k:
#         v+=i
#     print(v)
#     return v  #return  실행하고 나면 실행결과를 나를 부른애한테 되돌려줘, 되돌린다는 의미는 do_test에 900을 써넣은 것과 같은 의미, 항상 return값이 있는 
#     #리턴값이 있는 함수는 어디다 담아야 프린트함 어떤 변수에 담아서 씀, 출력할 거라면 바로 출력
#     #이것가지고 뭔가 하려면 변수에 담아서 써야함. 
#     #전달할 때 이

#     def do_test():
#         pass 
#     do test1(name="홍길동", age=20)  #이 값을 주고 싶어요. #매게변수 여러개 올 수 있어 딕션어리를 밸류만이면 
#     #나이 몇달 함께 갖고 싶어요, 이거랑 묶어서 딕션어리 모두 다 쓰고 싶어요, 그때 딕션어리 쓰면 되고 딕션어리받아줄 거야, 그럴 때는 
    #"**" kw 혹은 kw키워드아규먼트 kwargs관습적으로 씀 긴 단어를 줄어서 전달되지 않아?   관습-- 
    
    def do_test(**kwargs):
        for key, val in kwargs.items():
            print("key :", key, "value :", val)

    do test1(name="홍길동", age=20) 
    

        
    