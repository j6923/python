#import 뒤에 어떤 걸 가져올 거야. 쓰기 , 남이 만든 것 가져옴 
import turtle as t 

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
# t.mainloop()  #계속 반복되   #반복문으로 쓸 수 있음 


t.shape('turtle')
t.color("red")
for i in range(4):
    t.forward(100)  #100만큼 앞 가 
    t.right(90) #90도 각도로 틀어 
#t.mainloop()
#t.fd(50)

t2 = t.Pen()  #pen 모양 나옴, 새로운 펜 대문자임
t2.shape("turtle")
t2.color("#ff6600")
t2.penup()                                             #penup 이동하고 pendown 글
t2.goto(-200,100)  #좌표여서 ','임 
t2.pendown()
t2.begin_fill()
t2.fillcolor("red") #빨간색으로 채울거예요. 
t2.circle(25) #반지름 
t2.end_fill() #채우기 끝 




t3 = t.Pen()
t3.shape("turtle")
t3.shapesize(3)
t3.color("blue")
t3.penup()
t3.goto(100, 100)
t3.pendown()
t3.fd(100)
t3.rt(72)
t3.fd(100)
t3.rt(72)
t3.fd(100)
t3.rt(72)
t3.fd(100)
t3.rt(72)
t3.fd(100)
t3.rt(72)
t3.fd(100)





t4=t.Pen()
t4.shape("turtle")
t4.penup()
t4.goto(200,100)  #100도만큼 튼 것 
t4.pendown 

t4.circle(20,100 ) #반지름
t.mainloop()