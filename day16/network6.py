#클라이언트 사이드 

from socket import * 
ip = "192.168.0.31"
port = 5000 


def send(sock):   #send라는 함수를 만들고 
    sendData = input(">>>")
    clientSock.send(sendData.encode("utf-8"))
    #클라이언트 소켓으로 보낸다. 데이터를 encode는 보내는 애, utf-8로 변형해서
def recive(sock):
    recvData = clientSock.recv(1024) #클라이어트 소캣으로 받음을 recvData에 대입 
    #나중에 유지가 안됨 
    #클라이언트에서 받아줘야함 받아주는 것 
    print("서버가 보낸메세지:",recvData.decode("utf-8"))
#decode(utf-8)--메세지 받을 때 utf-8로 변환해줘. 
clientSock = socket(AF_INET,SOCK_STREAM) 
clientSock.connect((ip,port))#클라이어트 소켓을 

print("접속 완료")
while True:   #참이면 무한루프 돌림. 
    send(clientSock)
    recive(clientSock) #clientsock을 

#함수로 만든 이유 : 동시에 처리를 하기 때문에 쓰레드처리를 하면 함수로 하는것이 편함.  