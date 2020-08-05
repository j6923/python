import time #중간에 하면 안돼? 보통 위에 함, 사람들 보통 분석할 때 사용되는 변수 설명들 써봄. 중간에 내려보지 않아. 


class ATM:
    def __init__(self):
        print("초기화 함수 호출됨")
        self.balance = 0 #계좌잔액
        self.name = "홍길동" #임금주 


    def deposit(self,money ) :  #임금
        self.balance += money  #valance에 내용 저장하면됨. 
        print(money, "원 입급합니다.")
        print("현재 잔액:" , self.balance)

        with open("bank.log","w",encoding = "utf-8")as file:
            file.write(time.ctime() + "출금 :" +str(money)+"잔액: "+str(self.balance)) 
            #입금에도 기록을 남기고 싶어요. 
    def withDraw( self, money ) :  #출금 
        #db에 연결해서 현재 진짜 잔액이 존재하는지
        #권한이 있는지
        #감사기록을 남긴다. 
        print(time.ctime())    
        with open("bank.log","w",encoding = "utf-8")as file:
            file.write(time.ctime() + "출금 :" +str(money)+"잔액: "+str(self.balance)) #리스트면 writeline
#with open("./day10/back.log", "w", encoding="utf=8")as file:
        #with open("파일명", "모드",endco) as file:
        #현재작업디렉토리에 bank.log파일을 생성
        #지금시간, 출금액, 현재 잔액 저장하는 파일을 만들고 싶어요. 
        if self.balance >= money: #
            self.balance -= money 
            print(money, "원 출금합니다.")
        else:
            print("안 줘 ^^")
        print("현재 잔액 : ", self.balance)
auto = ATM()

print(auto)

auto.deposit(100)

auto.withDraw(10000) #money에 전달될 때 



#read, write, append 넣을 수 있어요. 
#코드 중복 쓰고 싶은 별도의 함수 만들어 놓고 거기있는 거 불러오고 import불어와서 하면 좋죠. 