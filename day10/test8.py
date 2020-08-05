class GuGuDan: 
    #a-zA-Z0-9 #두개이상단어.. print data >>> 공백넣으면 다른 단어됨. '_'넣으면 

    #printData와 같이 앞에 대문자로 해서 띄어쓰기 있어 표시하기도 
    def __init__(self):
        self.dan = 2 #아무것도 입력 안 하면 무조건 

    def print(self):
        for i in range(1,10):
            print(self.dan, "*", i,"=", self.dan*i)


g = GuGuDan()

g.dan = 7

g.print()

        







