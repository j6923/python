while True:
    value = int(input("숫자를 입력:"))                         #true이면 무한 반복 
     #5의 배수인가요
    if value%5 == 0:                                            #==비교 =대입 
        print(str(value)+"는 5의 배수입니다." )
        break                                                   #안 넣으면 빠져나오지 않음. 
    else:                                                        #만족하면 print(str(value))하고 아니면 break 탈출함. 
        print(str(value)+"는 5의 배수가 아닙니다")


        

        
        #ctrl +c 중단 ----> break (아래에)

print("이제 그만...^^")       
    