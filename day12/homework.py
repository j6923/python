#클래스 : 객체에 대한 설계도의 역할 
# 객체는 사물, 모델링  
#인스턴스 : 프로그램에 들어와서 메모리에 할당된 애, 
# 
# 
# 
# 2.  아무것도 없는  Cat 클래스를 정의하세요   
#클래스 cat (X)


#3. 나오게 추가 
#. 이렇게 쓸거예요. 뭐라고 주면 실행코드만 쓴 것 method 이름과 매게변수 뭔지 
# 
# # 이렇게 하면 이렇게 
# 


# 3.  다음 코드로 야옹야옹 이라는 메세지를 출력하도록 Cat 클래스를 수정하세요 
    #  nabi = Cat()
    #  야옹야옹   
# 4. 
#       nabi.play("공")
#      공을 가지고 놀고 있다냐옹 
class Cat():
    def __inti__(self):
        pass
    def calling(self):
        print("야옹야옹")
    def play(self,what):
        print(what+"을 가지고 놀고 있다냐옹")
nabi = Cat()
nabi.calling()
nabi.play("공")
# 5.   생성자 추가 
#      nabi2 = Cat("나비", 2)
#6. print(nabi2)
    # 이름 : 나비 , 나이 : 2 
class Cat():
    def __init__(self,name,num):
        self.name = name
        self.num = num 
    def eat(self,what):
        print("나비가", what +"을 먹고 있어요")

nabi2 = Cat("나비", 2)

print(nabi2)
    # 이름 : 나비 , 나이 : 2 
    # print(nabi2)
    # 이름 : 나비 , 나이 : 2 


# 7. 
#      nabi2.info()
#     이름 : 나비 , 나이 : 2 


# 8.nabi2.eat("생선")
# 나비가 생선을 먹고 있어요 
nabi2.eat("생선")

9.
     del  nabi2 
     고양이 죽는다 야옹 


if del nabi2:
    print("고양이 죽는다 야옹 ")
else:
    pass 

del nabi2 
# 10.  Customer 인스턴스를 생성할수 있도록 클래스를 정의하세요 
#       c =   Customer ("홍길동", 20, "990101-1234567")

class Customer():
    def __init__(self,name,age,identi):
        self.name = name
        self.age=age 
        self.identi = identi 

    def withDraw(self):




# 11. 
#       c.show()
#      # 홍길동님 현재 잔액은 0원입니다. 

# 12. 
#        c.deposit(5000)
#      # 홍길동님 계좌에 5000원 입금합니다.
#      # 홍길동님 현재 잔액은 5000원입니다. 

# 13.
#        c.withDraw(9000)
#     # 잔액이 부족합니다. 
#      # 홍길동님 현재 잔액은 5000원입니다. 

# 14.
#     c.withDraw(2000)
#     # 홍길동님 계좌에 2000원 출금합니다.
#      # 홍길동님 현재 잔액은 3000원입니다. 

# 15.
#        Customer 클래스에 인스턴스 속성의 값을 을 수정할수 있는 setter, getter 
# 	클 추가합니다. 
#       print(c.get_balance()) # 잔액값 가져오기 : 3000
#       c.set_balance(30000) # 잔액을 30000으로 변경 

# 16.
# 	5회 입금할때마다 
# 	잔액의 5%씩 이자 발생 
# 	c.deposit(1000)  #   31000
# 	c.deposit(3000)  #   34000
# 	c.deposit(2000)  #   36000
# 	c.deposit(2000)  #   38000
# 	c.deposit(3000)  #   41000
# 	# 이자발생   # 43050

# 17.
# 	del c 
# 	# 그 동안 이용해주셔서 감사합니다 
# 	# 계좌 잔액 : 43050 





