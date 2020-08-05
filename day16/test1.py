#서버 사이드 #서버 쪽

from socket import *

#어차피 자기 컴퓨터 포트 번호만 있으면 됨. 
port = 5000
serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind(("",port)) #포트번호
serverSock.listen(1)

print("%d반 포트로 접속 대기중"%port)


connectionSock,addr = serverSock.accept()

print(str(addr),"에서 접속되었습니다.")

#무한반복해서 들음. 

while True: #계속 수신 (무한루프)
    recvData = connectionSock.recv(1024) #상대방의 것 들음
    print("클라이언트가 보낸메세지:",recvData.decode("utf-8"))

    sendData = input(">>>") #보낸 것 다시 보냄 
    connectionSock.send(sendData.encode("utf-8")) #철저하게 순번지키도록 되어있음. 보낼 때까지 못 보냄 