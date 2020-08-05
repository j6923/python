#서버 사이드 
from socket import * #소켓에서 전체 불러옴. 
import threading #쓰레드 불러야 하니까 
import time 
port = 5000 #포트는 5000번

def send(sock): #발송하는 부분도 함수로 만들고 수신하는 부분도 함수로 만듦 
    sendData = input(">>>")
    sock.send(sendData.encode("utf-8"))


def recive(sock):
    recvData = sock.recv(1024)#버퍼의 크기, 정수니까 엄청크게 줄수도 있음. 
    print("클라이언트 메세지:", recvData.decode("utf-8"))


serverSock = socket(AF_INET,SOCK_STREAM)#소켓에 두개 매게 변수 줌
serverSock.bind(("",port)) #포트번호
serverSock.listen(1) #

print("%d반 포트로 접속 대기중"%port)


connectionSock,addr = serverSock.accept()

print(str(addr),"에서 접속되었습니다.")

sender = threading.Thread(target=send,args=(connectionSock,) )#수신#thread 튜플, 까지 줘야 튜플
receiver = threading.Thread(target=recive,args =(connectionSock,))#발신

sender.start()
receiver.start()
while True:
    time.sleep(0.1)
    pass
 