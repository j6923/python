#클라이언트 사이드 

from socket import * 
import threading
import time 
ip = "192.168.0.68"
port = 5000 


def send(sock):
    sendData = input(">>>")
    clientSock.send(sendData.encode("utf-8"))
    
def recive(sock):
    recvData = clientSock.recv(1024) #클라이어트 소캣으로 받음을 recvData에 대입 
    #나중에 유지가 안됨 
    #클라이언트에서 받아줘야함 받아주는 것 
    print("서버가 보낸메세지:",recvData.decode("utf-8"))
#decode(utf-8)--메세지 받을 때 utf-8로 변환해줘. 
clientSock = socket(AF_INET,SOCK_STREAM) 
clientSock.connect((ip,port))

print("접속 완료")
sender = threading.Thread(target=send,args=(clientSock,))#받는 쓰레드 줌
#send 아규먼트
receiver = threading.Thread(target=recive,args=(clientSock,)) #주는 쓰레드 줌 

sender.start()
receiver.start()

while True:    
    time.sleep(0.1)
    pass

#함수로 만든 이유 : 동시에 처리를 하기 때문에 쓰레드처리를 하면 함수로 하는것이 편함.  #

#데이터주고 받음 
#동시에 여러사용자 처리할 수 있도록 함. 
#튕겨나가는 것도 처리해줘야 함. 