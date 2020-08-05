#서버에서 
import socket #소켓하려고 소켓불러옴 
import threading #쓰레딩하려고 쓰레딩불러옴 

#접속정보 
host = "" #서버니까 제 로컬 
port = 5000


#서버 시작
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port)) 
server.listen()


#여러사용자의 접속 허용 
#client접속기록(정보)을 갖고 있는 리스트필요 
clients = [] #접속된 있는 애들에게 쭉 나눠줄게, 하는 것 있어야 함.
#서버는 중재역할만 함, 누가 보내면 접속한 모든 사람에게 보내주면 됨.  
nicknames = []
#브로드케스트라고 함, 서버가 모든 사람에게 보내주는 것을 
#접속 중인 모든 사용자에게 메세지 전달---브러드케스트 
def broadcast(msg): #메세지 주면 모든 애에게 줌 
    for client in clients: #클라이언트 리스트 
        client.send(msg) #전달함.  

#클라이언트의 메세지 처리하는 함수 :핸들러라고많이 함
def handle(client):
    while True:
    #클라이언트 메세지 수신
        msg = client.recv(1024) #개의 리스트 받아서 
        broadcast(msg) #전달함.  
        print(msg) #잘 되는지 출력  
    #브로드케스트 시켜줌
    #화면에 출력 
    #반복하는 함수



#리스닝 함수 
def receive():
    while True:
    
        connectionSock,addr=server.accept() #연결되면 소켓과ip정보 줌
        print(str(addr)+"로부터 연결됨")

        #별명을 요청하고 저장

        connectionSock.send("NICK".encode("utf-8"))
        #접속하자마자 별명을 보내
        nickname = connectionSock.recv(1024).decode("utf-8") #받음 
        print(nickname)#잘 가져왔는지 찍어 
        #별명 리스트에 별명담기 
        nicknames.append(nickname)
        #접속 소켓 리스트에 현재 소캣을 담기 
        clients.append(connectionSock) #여기에 저장해야 브로드케스트할 때 꺼낼 수 있음.

        #접속자 소개해주기 
        broadcast("{}님이 접속하셨습니다.".format(nickname).encode("utf-8"))
        connectionSock.send("서버에 접속되었습니다.환영합니다.".encode("utf-8"))#이 글자에 인코딩해줌
        #핸들림 함수를 쓰레드 
        t = threading.Thread(target=handle,args=(connectionSock,))
        t.start()

receive() 

#append 시키다보니까 사용자는 나갔는데 계속 보내려고 시도해서 에러뜸 
#사용자가 나가면 

#tjqjrk 보낼 때 사용자가encode 사용자가 한 채 보내야 