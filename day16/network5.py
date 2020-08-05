#서버 사이드 
from socket import * #소켓에서 전체 불러옴. 
port = 5000 #포트는 5000번

def send(sock): #발송하는 부분도 함수로 만들고 수신하는 부분도 함수로 만듦 
    sendData = input(">>>") #sendData에 사용자에게 >>>보여주고 내용을 입력받음
    sock.send(sendData.encode("utf-8")) #sock.send에 


def recive(sock): #소켓을 매게변수로 받음??? 
    recvData = sock.recv(1024)#버퍼의 크기, 정수니까 엄청크게 줄수도 있음. 
    print("클라이언트 메세지:", recvData.decode("utf-8"))
#받으면 "클라이언트 메세지:"하고 클라이언트의 메시지를 utf-8형식으로 받음

serverSock = socket(AF_INET,SOCK_STREAM)#소켓에 두개 매게 변수 줌
serverSock.bind(("",port)) #포트번호
serverSock.listen(1) #서버소켓에 listen 

print("%d반 포트로 접속 대기중"%port) #port를 출력하고  반 포트로 접속대긴중 


connectionSock,addr = serverSock.accept() #서버소켓을 받는 것을 소켓과 IP주소를 받음 

print(str(addr),"에서 접속되었습니다.") #addr를 문자로 출력하고 "에서 접속되었습니다"

while True: #참이면 무한루프돌림 
    recive(connectionSock) #연결소켓을 받고 
    send(connectionSock)  #연결소캣을 보냄
    #이게 참이면 무한루프 