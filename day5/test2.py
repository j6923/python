from turtle import * 

name = textinput("이름", "당신의 이름을 입력하세요.") #이름은 위에 문구는 아래 
print(name)
shape('turtle')
color('#ff6600')

lt(90) 

#몇 개의 명령들을 모아서 이름을 부여해놓은 것 : 함수
# 자주 사용하는 기능에 이름을 부여해 놓는 것
# 
# 파이션은 def 이름():
#              처리할 문장 
#  
#from trutle import * 해도 똑같이 나옴

def w(): #평상시에 실행 no, 내가 실행해 할 때만 실행함.  
    fd(50)

def d():
    rt(90)
    fd(50)
def a():
    lt(90)
    fd(50)
def s():
    lt(180)
    fd(50)

#df누르면 왼쪽 

onkey(w,"w") #함수와 키 연결  #w키를누르면 w(함수)를 호출해줘. 
onkey(d, "d")
onkey(a,"a")
onkey(s,"s")
listen() #써야 내가 입력하는지 안 하는지 잘 들을 수 있음. 

mainloop()