
#클라이언트 사이드 
from socket import *
#ip = "127.0.0.1" #연결할
ip ="192.168.0.31" 
port = 5000
#변경할수 있는 옵션 변수 등 변경 많은 애들은 위에 따로 설정

clientSock = socket(AF_INET,SOCK_STREAM)
clientSock.connect((ip,port)) #튜플해야함.  
# for i in range(1,65535):
#     try:
#         clientSock.connect(("119.205.197.57", 5000,i))
#     except:
#         print("괜찮아, 테스트잖아...힘내..")
    #사용하는 포트인지 응답하는 포트인지 다름. 
    #번호 예외 접속이 거부와 사용하고 있어서 인것은 다름.
    #서버가 준비안되어있어서 그 포트 쓰고 있어서 하는것이랑 에러가 다름. 
    #사용하고 있어의 예외가 나오면 그 포트를 쓰고 있다는 것. 
    #사용하는 포트와 안 쓰는 포트 구별가능
    #포트스킨이라고 함. 
    #포트스캔틀로 사용할 수 있음. 
print("접속완료")
while True:   #참이면 무한루프 돌림. 
    sendData = input(">>>") #메세지를 보냄, INPUT으로 >>>값을 넣고 내용을 입력받음 
    clientSock.send(sendData.encode("utf-8")) #utf-8형식으로 변환해서 보냄. 
    recvData = clientSock.recv(1024) #클라이어트 소캣으로 받음을 recvData에 대입 
    #나중에 유지가 안됨 
    #클라이언트에서 받아줘야함 받아주는 것 
    print("서버가 보낸메세지:",recvData.decode("utf-8"))