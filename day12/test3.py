#에러 
#0~9사이의 정수를 램덤하게 생성
#예외란? 프로그램 실행 중 발생한 예상치 못한 오류. 
#예상치 못한 오류 : 가벼운 오류 
#예외를 처리 해줄 수 있다. 

#예외처리는 case by case 

#예외가 발생하려는 지역을 try 
#   try:
        # 문장1  여기에 문제가 발생가능해 
        # 문장1
    #except ????
    #      예외처리문장1
    #      예외처리문장2   이렇게 처리해 
# import random
 
# n = int(input("숫자입력:")) #사용자의 입력값은 문자임, 그래서 연산불가.
# #int빼면  
# a = random.randint(0,9) #램덤한 정수를 0-9까지 넣고 싶어요. 

# print(n/a)
# # 수학에서는 0으로 나눌 수 없어요. 
#사용자 저의형 예외 
# execpttion을 상속받음 
class EvenError(Exception): #부모클래스가 없는데 bultin 내장  exception 
# base exception이고 아래 exception 때땨 자동으로 발생 exception 
#내장 되어 있어서 안 써도 됨, 상속 받음, 에러를 
#특별한 예외일어나면 예외일어나도록 함,----> 예외 처리 
#원래 에러가 아닌 것을 에러처럼 취급하고 싶으면 
#어떤 조건이 되면이런if  예외 일으켜 raise 클래스명 
# except ~는 어떻게 해 뒤에 어떻게 처리해 라는 처리 문장  
    def __init__(self,msg):  
        self.msg = msg 
#생성자 33 
    def __str__(self): #사용하는 msg받으라고 하고 그 문구를 리턴하게 함
        return self.msg #(뒤에 에러메세지정할 수 있음.  )
        #매게 변수로써 
        
    #생성한 때랑 에러 뿌려지는시점 다를 수 있음. 
    # 초기화 함수 쓰는 것은 잘 보기 위해서 
    # 평상시에는 안 씀.  
import random 
try : 
    n = int(input("숫자입력:"))
    for i in range(10): #한 열번 돌리면 그중 예외 나올 수 있음. 
        a = random.randint(0,9)
    print(n/a)
    if n %2 == 0:   #만약 n을 2로 나눈 
        raise EvenError("짝수만 입력해라...--")  #이걸 일으켜
    #생성자를 호출, 저 문자열을 33의 msg로 전달 
    msg 인스턴스 변수에 저 메세지 있음 
    #위에 저렇게 쓰고 뒤에 문자 넣으면 가능  
except EvenError as ee: #사용자 정의어 제외 원래 시스템상에러가 아니라 내가 에러처럼 처리하고 싶다면 만들어쓰기 
    print(ee) #출력해 라고 하면 이 때 36번 해서 정의놓음 저 함수 호출
    #이거의 이름을 이거라고 하고 찍어봐 
    print("짝수는 계산 안해줘")


    
except ValueError:#여러개가 있을 수 있음
    print("숫자만 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌 수 없음")

finally:
    print("이 부분은 예외가 있던 없던 항상 실행됩니다. ")
    #예외가 있던 없던 반드시 실행하는 것주고 싶을 때  
    #
#except는 여러개 줄 수 있음. 

    #ZeroDivisionError 이런게 일어나면 except print 0으로 나눌 수 없음 
    #이렇게 처리해 

    #valueerror 이름, 

    #2.지원하는 package있지만 공부할 사람 3으로 공부하세요 


#예외가 아닌데 예외로 처리하고 싶어요 

#사용자가 입력한 값이 짝수이면 실행안함. 

