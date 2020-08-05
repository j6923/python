# 1. 1부터 100까지 출력 
print(list(range(1,101)))
#2.11111
#22222
#33333
#44444
#55555
#for i in range(1,101):     #어차피 반복하니까 list사용 안 해도 됨 
    #print(i*5)

msg = ''
for i in range(1,6):
    msg = msg+str(i)   
    print(msg)


#3
# 99999
# 88888
# 77777
# 66666
# 55555
v = range(9,4,-1)    #10부터 1까지 증가폭 -1 
msg1 = ''                #msg1은 none
for i in v:
    msg1 = str(i)*4                #반복해라 
    print(msg1)
   

print("----------------------------------------------------")
#4.  이중for문 사용 
#1234
#5678

for i in range(1,3):
    for j in range(i+1):
        print(str(i)*4)
 #4개 나오고 enter 
 #옆으로 붙여 4개 나오면 enter 
# for j in range(1,6):
#     for i in range(1,6):
#         print(j,end="")
#     print()


#5. 구구단8단 출력 
#8*1 = 8
#8*2 = 16
#8*3 =24 
#8*4 = 32 
#8*5 =40
#8*6=48
for i in range(1,10):
    print("8*",i,"=",8*i)




