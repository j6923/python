
class monkey: 
    def __init__(self):
        self.eyes = 1
        self.ears = 2
        self.mouth = 1
        self.tale = 1
        self.species = "긴꼬리원숭이"
        self.age = 3
        self.hand = 2 
    
    def climb(self):
        print("나무를 타요")
    
    def eating(self):
        print("잡식성")
    
    def sleeping(self):
        print("쿨쿨 자요")


m = monkey() 

print(m.eyes)
print(m.ears)
print(m.mouth)
print(m.tale)
print(m.species)
print(m.age)
print(m.hand)

m.climb()
m.eating()
m.sleeping()

