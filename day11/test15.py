from turtle import *
from random import randint
a = Turtle()
screen = Screen()
print(a)
print(screen)


screen.addshape("audience.gif")#한가운데 이미지가 들어감
screen.addshape("turtle.gif")#안 넣으면 이미지 안 뜸. 
a.shape("audience.gif") #한가운데 이미지가 들어감 # 파이썬에 이미지 갖다 놓기
a.penup() 
a.goto(0,230) #어디로 갈거예요로 이미지 옮길거예요,정중앙기준으로 가운데 4,4가 0,0 위는 0,


t1 = Turtle()
t1.color("red")
t1.shape("turtle") #토끼이미지 넣으면 토끼경주, 지렁이 경주도 가능함. 
t1.penup()
t1.goto(-400,0)
t1.pendown()
t1.write("1번 꼬부기")

t2 = Turtle()
t2.color("green")
t2.shape("turtle") #토끼이미지 넣으면 토끼경주, 지렁이 경주도 가능함. 
t2.penup()
t2.goto(-400,-50)
t2.pendown()
t2.write("2번 꼬부기")

t3 = Turtle()
t3.color("yellow")
t3.shape("turtle") #토끼이미지 넣으면 토끼경주, 지렁이 경주도 가능함. 
t3.penup()
t3.goto(-400,-100)
t3.pendown()
t3.write("3번 꼬부기")

t4 = Turtle()
t4.color("blue")
t4.shape("turtle") #토끼이미지 넣으면 토끼경주, 지렁이 경주도 가능함. 
t4.penup()
t4.goto(-400,-150)
t4.pendown()
t4.write("4번 꼬부기")

t5 = Turtle()
t5.color("black")
t5.shape("turtle") #토끼이미지 넣으면 토끼경주, 지렁이 경주도 가능함. 
t5.penup()
t5.goto(-400,-200)
t5.pendown()
t5.write("5번 꼬부기")

t6 = Turtle()
t6.color("gray")
t6.penup() 
t6.goto(-350, 30)
t6.speed(8)

for i in range(9):
    t6.pendown()
    t6.rt(90)
    t6.fd(300)
    t6.bk(300) #backward라고 써도 됨.
    t6.lt(90)
    t6.penup()
    t6.fd(50) 
    
    
    

t6. goto(1000,1000)
#n이 입력한 것을 받아야 실행 
n = textinput("골라", "어떤 거북이에게 응원하실건가요?")  #쓰는 것 나옴. 
a.color("red")
a.write(n+"번 꼬부기 이겨라", left)
dis1 = 0
dis2 = 0
dis3 = 0
dis4 = 0
dis5 = 0

for i in range(250): 
    rnd1 = randint(1,5)
    rnd2 = randint(1,5)
    rnd3 = randint(1,5)
    rnd4 = randint(1,5)
    rnd5 = randint(1,5)
    
    dis1 += rnd1
    dis2 += rnd2
    dis3 += rnd3
    dis4 += rnd4
    dis5 += rnd5 
    
    t1.fd(rnd1)
    t2.fd(rnd2)
    t3.fd(rnd3)
    t4.fd(rnd4)
    t5.fd(rnd5)
    if (dis1>=400):
        t1.penup()
        t1.goto(0,100)
        t1.pendown()
        t1.shape("turtle.gif")
        break
    elif dis2 >= 700:
        t2.penup()
        t2.goto(0,100)
        t2.pendown()
        t2.shape("turtle.gif")
        break
    elif dis3 >= 700:
        t3.penup()
        t3.goto(0,100)
        t3.pendown()
        break
    elif dis4 >= 700:
        t4.penup()
        t4.goto(0,100)
        t4.pendown()
        break
    elif dis5 >= 700:
        t2.goto(0,100)
        break
    
    
#     for i in range(250): 
#     t1.fd(randint(1,5))
#     t2.fd(randint(1,5))
#     t3.fd(randint(1,5))
#     t4.fd(randint(1,5))
#     t5.fd(randint(1,5))
t1.write(dis1)
t2.write(dis2)
t3.write(dis3)
t4.write(dis4)
t5.write(dis5)

mainloop()