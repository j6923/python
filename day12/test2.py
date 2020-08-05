# del c1 #소멸자 호출 #생성자: 


class Car:
    def __init__(self):
        print("초기화 함수")
    
    def __del__(self): #더 이상 이 객체 사용 안함 
        print("소멸자 호출 : 더이상 안 써요.. 폐차 ")

    #def __del__(): #소멸자 
    def __str__(self):
        #문자열화해 반환
        return "str method 가 호출됨"

    #매직함수(메서드):가장 일반적인 용도: 오퍼레이터 오버로딩용 가장많이 쓰임
    # +:__add__
    # - : __sub__
    # * : __mul__
    # / : __turediv__
    # // : __floordiv__   #div는 나누다라는 뜻 
    # % : __mod__
    # ** : __pow__
    # < : __lt__ #less than 
    # > : __gt__
    # >= :__ge__
    #


c2=Car()
print(str(c2)) #이 객채를 스트링으로 바꿔 

#소멸자 호출의 용도는 메모리에서 이 객체를 제거, 즉 인스턴스를 없애는 것 

del c2 



