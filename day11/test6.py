class Whale:
    def __init__(self):
        self.eyes = 2
        self.mouth = 1
        self.nose = 2
        self.tail = 1
        self.speices = "범고래"

    def eating(self):
        print("새우를 먹어요")

    def sleeping(self):
        print("어디에서 잘까요?")
    
    def swimming(self):
        print("헤엄을 잘 쳐요")
    
    def breathing(self):
        print("잠깐 올라와요")

w = Whale()

print(w.eyes)
print(w.mouth)
print(w.nose)
print(w.tail)
print(w.speices)

w.eating()
w.sleeping()
w.swimming()
w.breathing()