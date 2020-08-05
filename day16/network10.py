#클라이언트 사이드
from socket import *
from threading import *

#ip = '192.168.0.68'
ip = '192.168.0.37'
port = 5000
nickname = input("당신의 닉네임을 입력하세요 : ")

clientSock = socket(AF_INET,SOCK_STREAM)
clientSock.connect((ip,port))
print("접속완료")

#서버에 닉네임 보내기
def receiver():
    while True:
        try:
            msg = clientSock.recv(1024).decode("utf-8")
            if msg == "NICK":
                clientSock.send(nickname.encode("utf-8"))
            else:
                print(msg)
        except:
            print("에러발생 연결끊음")
            clientSock.close()
            break

#서버에 메세지 보내기
def send():
    while True:
        clientSock.send("{}:{}".format(nickname,input()).encode('utf-8'))

Thread(target=receiver).start()
Thread(target=send).start()
'''
#클라이언트 사이드 
from socket import *
from threading import *
ip = "192.169.0.68"
port = 5000
#닉네임 결정 

nickname = input("당신의 닉네임을 입력하세요 : ")

#서버에 연결
clientSock = socket(AF_INET,SOCK_STREAM)
clientSock.connect((ip,port))


#서버에 닉네임 보내기 

def receive(): #서버가 나에게 보내주는 것이 있으면 받아주는 함수 
    while True:     #여러번 하기 때문에 반복문
        try:
            msg = clientSock.recv(1024).decode("utf-8")
            if msg =="NICK":
                clientSock.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            #에러 발생시에 연결끊기 
            print("에러 발생") #에러발생하면 
            clientSock.close() #현재접속끊고 
            break #반복문 탈출 

    #서버에 메세지 보내기 
def send():
    while True:
        msg = "{}:{}".format(nickname, input(''))
        clientSock.send(msg.encode('utf-8'))

    #수신과 발신을 동시에 처리하기 위해 쓰레드 

receive_thread=threading.Thread(target=receive,args=(clientSock,))
reveive_thread.start.start()

send_thread = threading.Thread(target=send,args = (clientSock,))
send_thread.start()

        
        
        
        #이렇게 해석한 애가 메세지 
        #첫글자가 nick이면 별명을 보내라는 거구나 
        # #이거 일때 send해서 닉네임을 encoding해서 보냠 
'''