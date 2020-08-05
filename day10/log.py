import time


def saveLog(savedir, money, balance, mode) :
    if mode:
        type = "출금"
    else:
        type = "입금"
        with open(savedir,"w",encoding = "utf-8") as file:
            file.write(time.ctime() + type +str(money)+"잔액: "+str(balance)+"\n") 


            #동일한 코드 별도의 모쥴로 만들고 필요한 시점에 불러옴. 
            #