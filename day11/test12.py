class parent:                                                             #클래스 parent를 생성
    def __init__(self):                                                   # 초기화함. 
        self.name = "홍판서"                                               #이름을 홍판서라고 함
        self.age = 60                                                      #나이를 60으로 함
        self.height = 190                                                   #키를 190으로 함
        self.gender = "남"                                                  #성별을 남으로 함
        self.nation = "조선"                                                 #국적을 조선으로 함. 

    def eating(self):                                                      #먹는 동작을 eating이라는 함수로 만듦
        print("냠냠 맛있게 먹어요")                                          #함수가 호출되면 냠냠 맛있게 먹어요를 출력 
    def sleeping(self):                                                     #자는 동작을 sleeping이라는 함수로 만듦
        print("쿨쿨 자요")                                                   #함수가 호출되면 쿨쿨 자요 
    def singing(self):                                                       #노래부르는 동작을 singing이라는 함수로 만듦
        print("아~~리랑 아~~리랑~~~~")                                        #함수를 호출하면 아~리랑 아~리랑~~~출력 
        print("뽕짝   뽕짝~~~")                                               #함수를 호출하면 뽕짝 뽕짝~~~출력 
    def cooking(self):                                                       #요리하는 동작을 cooking이라는 함수로 만듦 
        print("조리 제조 스킬 1증가... ^^")                                    #함수를 호출하면 조리 제조 스킬 1증가...^^출력 

if __name__ == "__main__":                #여기에서만 하게끔 
    p= parent()                           #parent클래스를 p에 대입하여 p라는 인스턴스 생성 
    print(p.name)                         #p의 name을 출력 
    print(p.height)                       #p의 height를 출력 
