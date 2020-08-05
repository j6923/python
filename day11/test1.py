class Test:
    def __init__(self,balance): #인스턴스 변수 
        self.balance = balance

    def print(self):
        print("잔액 :" , self.balance)
    #실제 인스턴스 만드는 방법 변수명 = 클래스 명
    # t = test() 여기 클래스()를 참고로 생성자를 불러, 그런애들의 참조값 t를 갖음 

t = Test(500) #valance 500
t. aaa = 200
print(t.aaa) #인스턴스 변수이기 때문에 t라고 하는 애의 인스턴스 주소보고 메모리 번호 봄, 없으면 만들어 줌. 
t.print() #현재 값 알 수 있음 
print(t)