#ipconfig ---ip주소 찾음
#ip주소 0-255까지 
#

from socket import *
           
serverSock = socket(AF_INET,SOCK_STREAM) #두개의 매게 변수 같은 소캣
#통신하려면 포트있어야 함. 서브로 들어오는관문 
#65535개가 있음>>>포트가 
#65535 >>>> 8000-9000 port 개발용
#나머지 상용제품들이 상용하고 있음 
#쓰고 있는 것 포트 쓰면 충돌나서 서로 죽어버림. 
#확실히 안쓰면 써도되지만 그렇지 않으면 충돌남. 
serverSock.bind(('',5000)) #5000포트를 사용, 5000은 그냥 찍음#튜플로 줘야함.
print("사용자의 접속을 대기합니다.")
serverSock.listen(1) #사용자의 연결을 기다림(수신중...)
connectionSock,addr = serverSock.accept() #이렇게 연결할 거니 
#허용될 때까지 무한루프 탐 
print(str(addr)+"연결 성공!!!") #y눌러야 가능 
#상대방에 대한 정보는 

#powrshell로 앞전 창 갈 수 있음 

#connectonsock 상대방과 소통하는 객체 
data = connectionSock.recv(1024)#얼마단위로 받을 거냐크면 큰 데이터 ,작으면
#데이터 쪼개서 받음 
#print(data.decode("utf-8")) #decode(utf-8)은 우리가 읽은 수 있는
#utf-8로 제 가공 
#너무 커도 성능 나쁘고 작아도 성능 나쁨
msg = data.decode("utf-8") #data의 decode를 utf-8로 
print(msg)
connectionSock.send(msg.encode("utf-8")) #반사 
print("서버 메세지 전송 완료")


#print("hello\n \t world") 문자열 앞에 r 노데이터야 
#문자열 그대로 다 못주고 바이트단위로 끊어서 줌. 
#포장단위로 보냄--- 패킷이라고 함. 
#다 오면 제조업해서 1개 만들어서 받음. 


#리스트에 문자열 개 넣음, 램덤하게 하나 뽑을 수 있나 . 
