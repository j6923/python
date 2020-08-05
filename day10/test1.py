#프로그램에 취급되는 모든 사물은 object(객체).. 전산세계에서 어울리게끔 변수, 동작을 구분해서 만들어야 전산세계에서 만들 수 있음 
#class  -- 전산세계에서 사용할 수 있는 설계도 ,,   붕어빵의 틀 
#프로그램의 필요한 성질만 모아서 만듦. 
#객체가 어떻게 되어 있고 특성있을 거야 --- 객체 모델링 
#대상의 속성을 변수로 만듦, 행위나 동작은 함수로 만듦, 함수라고 하기도 하고 method라고도 함. 
#설계도 만드는 것 객체 모델링 
# class 클래스명:   ---> 
#     속성
#객체 : 사물 
# class : 설계도 
# 대상 : instance 

#     함수,method()
# class Human: (전)
#    pass
#c나 자바는 hong = new Human() 파이썬은 없음. 
     
class Human:
    #__메서드를 매직메서드 ---- 특정한 기능을 하는 특별한 method
    def __init__(self):
        print("초기화 함수")                            
    def eating(self):
        print("냠냠 맛있게 먹어요")
    def sleeping(self):
        print(" 쿨쿨.. 쿨쿨 zzzzz ")
        #첫번째 바로 self 들어와야 
#이 객체를 만들어 낼 때 자동으로 호출 
hong = Human()
#이 글래스로 실행해서 하나의 사물 hong을 실체를 만들어냄. 
#초기화한다고 해서 초기화 함수라고 함. init 따로 만드는 순간에 init자동으로 호출됨 
#실체를 전산에서는 instance라고 함. 메모리상에 실제 만들어지는 애.

print(hong)
hong.eating() # 이 함수로 출해, 동작함. 붕어빵 틀처럼 빵 찌어내듯이 만들어
# a = 10
# print(type(a))  #모든지 다 클래스를 통해 만들어진 것 

#동작을 하려면 __init__method 있어야 함 
hong.sleeping()


print("---------------------------------------------------------")
lucy = Human()
#하나 다 쓸려면 한 줄에 사람하나씩 딱딱 만드는 것 eating하고 sleeping같은 함수 들어가 있음 
lucy.eating()
lucy.sleeping()  #나, 함수할 때 s.append처럼 앞에 lucy들어가는 것.

