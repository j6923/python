print("1111111111111")   ##"1111111111111"을 출력해라  
def double(x): #사용자가 준 값을 x
    print("2222222222222") ##"2222222222222"을 출력하고 
    return x*2 #사용자가 뭔 값을 주면 2배하고  더블이라는 함수가 있어 정의만. 실행no 
print("3333333333333")   
# "3333333333333"  한줄씩 실행하해서 33333  

y = double(10) #더블이라는 함수 실행 2222 값을 전달해서 duble 10의 값을전달해서 호출해, x에는 10이 담겨있음 그리고 나서 22222를 출력해. x가 준 값이 10이면 4.
#4에 값을 20전달하고 2를 곱해 그리고 그 값을 return을 부른 double에 보내. 
#20을 출력해  
#나를 부른 애한테 값을 전달해.  그 함수가 실행되고 그 자리에 이 값을 보내 .  y = 20이 들어감 
print(y)

print("---------------------------------------------------------------------------------------------------------")
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