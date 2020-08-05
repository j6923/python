class Human:
    def __init__(self):
        print("초기화 함수호출")
        self.name = "고길동"
        self.age = 30
        self.job = "고위공직자"
        self.eye = 2
        self.mouth =1
        self.ears = 2
    def eating(self):
        print("냠냠 맛있게 먹어요")

    def walking(self):
        print("두발로 걸어요 아장아장")

    def sleeping(self): 
        print("쿨쿨 자요")
    
    def thinking(self):
        print("생각한다 고로 존재한다")  #라인 많음, 똑같은 코드도 중복 class하나 정리 
    def status(self): #상태정보, 항상 self로 접근 
        print("이름 :", self.name)
        print("나이 :", self.age)
        print("직업 :", self.job)
        print("눈 :", self.eye)
        print("입 :", self.mouth)
        print("귀 :", self.ears)
        
print(Human,id(Human), type(Human)) #클래스 매모리 상 여기 위치 class는 일종의 타입 

    #실제 사용하려고요 
ko = Human() #인스턴스변수 = 클래스명() #클래스의 초기화 함수가 호출 
#ko의 주소가 human()의 매게주소로 들어감. 자동으로
    #class 초기화
print(ko.name) #.연산자 의미 : 주소를 찾아가.. 주소 찾아가면 메인이라는 애가 있어요, 거기 가서 .name이라는 애 가져와 
    #이름을 출력하고 싶어요, 뭐라고 쓰면 되요? 
#method 호출 어떻게 ? >>>> ko.thinking() 이렇게 가져오면 됨. 
#나머지 변수값도 출력 
print(ko.age)
print(ko.job)
print(ko.eye)
print(ko.mouth)
print(ko.ears)
#함수도 호출 ,,, 
ko.thinking()
ko.walking()
ko.sleeping()
ko.eating()

ko.status()  #--> 한번에 상태정보 다 볼 수 있음 

#이런 애 하나 더 만들고 싶어요. 
#팽수
P = Human()
P.status()

#이름 나이 할 것 없이 다 만들어짐 
#불편한 점 : 자꾸 고길동이 됨 .
P.name = '팽수'
P.age = 10
P.job = "EBS 직장인" #바뀌어 있음. 인스턴스의주소가 달라 따로 가지고 있음, 함수는 class에 있는 것 같이 씀. 
#어디에 있는 건지 멤버값 줘야 함. 
#공통점은 같이 공유, 차이점
P.status()



