# import os   # === > 어제 8 복사   

# import log 
import time 

# print(os.getcwd())

class ATM:
    def __init__(self):
        print("초기화 함수 호출됨")
        self.__balance = 0 #내부에서만 사용되는 변수 , 자바는 private라고 함. 
        self.name = "홍길동" 
        self._account = 600   


    def deposit(self,money ) :  
        self.__balance += money  
        print(money, "원 입급합니다.")
        print("현재 잔액:" , self.__balance)

        
#변경하거나 값 수정하고 싶어 setter, getter
    def get__balance(self):
        #검사기록 
        print("잔액 :", self.__balance) #가져올 거예요. 
    def set__balance(self,balance):
        self.__balance = balance

    #감사기록 사용해 만들거예요     지정한 값으로 set 담는 것 누가 값 변경했어, 각종 기록 남길 수 있음. 
    
        
    def withDraw( self, money ) : 
        print(time.ctime())    
        

        if self.__balance >= money: #
            self.__balance -= money 
            print(money, "원 출금합니다.")
        else:
            print("안 줘 ^^")
        print("현재 잔액 : ", self.__balance)
auto = ATM()

print(auto)

auto.deposit(100)

auto.withDraw(10000) 
auto.aaa =300  #여기에 없는 변수 쓰면 하나 만들어줌  #그 동네에 변수 하나 내부변수는 아님. 잔액안 바뀜.
print(auto.aaa)
auto.set__balance(50000)
# print(auto._account)#_ 암묵적으로 밖에서 사용불가 --밖에서 볼수 있음. 
# print(auto.__balance) #__강제적으로 밖에서 사용불가 --밖에서 볼 수 없음. 
auto.withDraw(10000)
#변수에 때려 넣으면 기록 불가 
#함수 통하면 기록을 남기게 할 수 있지만 변수는 기록 남기지 않음. 
#외부에서 직접제어 안 했으면 좋겠어 내부에서 쓰는 겁니다. 그래서 변수 앞 _ 내부에서 사용할 거야 . 

#언더바 두개 강제적인 의미  -- 변수를 숨기는 용도로 사용할 수 있음. , 이 변수는 내부에서만 사용되는 변수 
#한개 외부 접근 안 하고 현재 클래스에서만 사용
#두개는 강제성을 띔. -- 이런 애는 없어, 에러 남. 
