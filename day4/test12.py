while True:
    value = int(input("숫자를 입력:"))                         #true이면 무한 반복 
     #5의 배수인가요
    if value%5 == 0:                                            #==비교 =대입 
        print(str(value)+"는 5의 배수입니다." )
        continue                                                   #이번엔 이걸로 끝이야, 계속 이어지는 애 
    else:                                                        #만족하면 print(str(value))하고 아니면 break 탈출함. 
        print(str(value)+"는 5의 배수가 아닙니다")


        
#숫자입력 if감 맞으면 continue 아니면 위로, 오늘은 이걸로 끝이야 그 아래 처리할 문장 있어도 패스하고 넘어감. 알수 없는 조건에 실행하는 것이 
#많을 때 더 이상 일 안 하게 할 때 이용함. 
        
        #ctrl +c 중단 ----> break (아래에)

print("이제 그만...^^")       



