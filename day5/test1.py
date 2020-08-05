import turtle as t 

t.color("red")
t.shape("turtle")
t.shapesize(1)
#t.delay(100) #지연되어서 실행되는 것 느리게 기다렸다가 움직이는 것 
t.speed(9)
t.fd(100)
dis = 100 #변수 줌 
rad = 90  #회전 각도 
for i in range(100): 
    dis +=5
    rad += 2
    t.rt(rad)
    t.fd(dis)

t.mainloop()

#20번 정도 반복 
