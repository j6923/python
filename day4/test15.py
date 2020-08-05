import turtle as t 

t.shape('turtle')
t.color("black")
t.circle(200)

t2 = t.Pen()
t2.shape("turtle")
t2.color("blue")
t2.penup()
t2.goto(100,200)

t2.pendown()
t2.circle(50)


t3 = t.Pen()
t3.shape("turtle")
t3.color("blue")
t3.penup()
t3.goto(-100,200)
t3.pendown()
t3.circle(50)


t4 = t.Pen()
t4.shape("turtle")
t4.color("black")
t4.penup()
t4.goto(100,200)
t4.pendown()
t4.begin_fill()
t4.fillcolor("green")
t4.circle(30)
t4.end_fill()




t5 = t.Pen()
t5.shape("turtle")
t5.color("black")
t5.penup()
t5.goto(-100,200)
t5.pendown()
t5.begin_fill()
t5.fillcolor("green")
t5.circle(30)
t5.end_fill()

t6 = t.Pen()
t6.shape("turtle")
t6.color("black")
t6.penup()
t6.goto(0,50)
t6.pendown()
t6.circle(100,60) #반지름 각도 
t6.circle(100,-120)

t7 = t.Pen()
t7.shape("turtle")
t7.color("black")
t7.penup()
t7.goto(0,50)
t7.pendown()
t7.begin_fill()
t7.fillcolor("black")
t7.rt(90)
t7.fd(20)
t7.rt(90)
t7.fd(20)
t7.rt(90)
t7.fd(20)
t7.end_fill()

t8 = t.Pen()
t8.shape("turtle")
t8.penup()
t8.goto(0,50)
t8.pendown()
t8.rt(90)
t8.fd(20)
t8.lt(90)
t8.fd(20)
t8.lt(90)
t8.fd(20)


# t3.rt(72) right
# t3.fd(100) forward 
# t3.rt(72) lt()는 left 
# t3.fd(100)
# t3.rt(72)
# t3.fd(100)

# t.shape('turtle')
# t.color("red")
# for i in range(4):
# t.forward(100)  #100만큼 앞 가 
# t.right(90) #90도 각도로 틀어 
# t.forward(100)                           #하고싶은 것 위에서부터 한줄한줄 넣기 90도임 
# t.right(90)                                         #ff6600 rgv칼라값  4번 
# t.forward(100)
# t.right(90)
# t.forward(100)
t.mainloop()  #계속 반복되   #반복문으로 쓸 수 있음 
