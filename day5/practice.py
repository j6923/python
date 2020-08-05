#두 개 주사위를 던졌을 때 합이 4가 되는 모든 경우의 수를 출력하는 프로그램을 작성하시오. 
#(1,3)
#(2,2)
#(3,1)
#이중 포문으로 하기 

#나
# print = range(1,7)
# dic = range(1,7)
# dic1= range(1,7)
# userInput = int(input("주사위 두 개를 던지 세요.: "))

# dic1 = range(1,7)
# for i in dic:
#     for j in dic1
#     print 

#수업
for i in range(1,7):
    for j in range(1,7):
        if i+j ==4:
            print("("+str(i)+","+str(j)+")")



# import random 
# li = [1,2,3,4,5,6,1,2,3,4,5,6]
# dic = random. randint(0,2)
# print 
# if dic+dic1==4:
#     print("dic", dic, "dic1", dic1)
# elif dic+dic1 != 4

#2. 특정 연도가 윤년인 윤년인지 프로그램을 작성하시오. 
#(단 윤년은 4년마다 한번씩 돌아오며, 100년단위로 윤년이 아니며, 400년단위로 윤년임)
#(EX) 1600년은 윤년이면 1900년은 윤년이 아님. 

#출력예 

#4, 8, 12, 16 ~~~ 윤년

# for i in range(1,2000):
#     if i %4 == 0 and i%100 != 0  or i%400 == 0  :
#         print(i, "는 윤년")
#     else: 
#         print(i, "윤년이 아님")

        #and는 둘 다 만족 i%100이면서 i%400인 조건 만족할 수없어 그래서 or 
        
#사용자의 입력받아 보는 것 
i = int(input("연도입력: "))
if i %4 == 0 and i%100 != 0  or i%400 == 0  :
    print(i, "는 윤년")
else: 
    print(i, "윤년이 아님")