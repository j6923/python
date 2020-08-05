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

if __name__=="__main__": 
    r = Rabbit()
    print(r.eyes)
    r.jump()
    r.eating()
    r.sleeping()

#test5== 원숭이
#test6 === 고래

