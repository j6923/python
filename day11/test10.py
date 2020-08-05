from test9 import animal 
class Animal:
    def __init__(self,foots):
        self.eyes = 2
        self.mouth = 1
        self.ears =2

    # def eating(self):
    #     print("당근을 먹어요")


class Rabbit:

    def __init__(self):
        print("토끼 초기화 함수")
        self.eyes = 2
        self.mouth = 1
        self.ears = 2
        self.species = "앙골라"
        self.name = "토순이"
    
    def jump(self):
        print("깡총깡총 뛰어요")

    def eating(self):
        print("당근을 먹어요")
    
    def sleeping(self):
        print("쿨쿨 자요")

    print(r.eyes)