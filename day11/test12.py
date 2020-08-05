class parent:
    def __init__(self):
        self.name = "홍판서"
        self.age = 60
        self.height = 190
        self.gender = "남"
        self.nation = "조선"

    def eating(self):
        print("냠냠 맛있게 먹어요")
    def sleeping(self):
        print("쿨쿨 자요")
    def singing(self):
        print("아~~리랑 아~~리랑~~~~")
        print("뽕짝   뽕짝~~~")
    def cooking(self):
        print("조리 제조 스킬 1증가... ^^")

if __name__ == "__main__":
    p= parent()
    print(p.name)
    print(p.height)
