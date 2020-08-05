import cx_Oracle #오라클연결되게 외부에서 함수가져옴. 

#print(cx_Oracle.init_oracle_client())
#연결 데이터 베이스에 connetion 연결되어 있는 상태를 connection이 설립되었다. 라고 함
# ip 통신 포트, id와 password필요
#connection = cx_Oracle.connect("id, "pw","서버ip:1521/db명")
#scott tigertiger 서버ip 1521 
connection = cx_Oracle.connect("scott", "tigertiger","orcl.cyb0gs2amyei.ap-northeast-2.rds.amazonaws.com:1521/orcl")
#id/pw  
#orcl.cyb0gs2amyei.ap-northeast-2.rds.amazonaws.com
print(connection)
#아마존 서버랑 연결이 된 상태 
# <cx_Oracle.Connection to scott@orcl.cyb0gs2amyei.ap-northeast-2.rds.amazonaws.com:1521/orcl>
# PS E:\dev\python_workspace>
# 
# #오라클 설치 안 한 상태면 아까 그거 설치하고 하면 됨.  


cur = connection.cursor()

query = "select* from dept" #사용할 sql문 
cur.execute(query)#커서를 통해 이 문장을 실행해 

for x in cur:
    print(x)

    #연결해주면 반드시 자원반납해줘야 함. 

#연결 끊기
 #db와의, 데이터베이스 나한테 명령 줬는데 명령 줄거라고 생각함.  
 #다 끊지 않고 대기하고 있음. 
 #자원 소모하고 있음--- 접속하는 애 많으면 동시접속자 제한 둠. 
 #접속초과 나올 수 있음. 

connection.close()
#아이오 network database는 쓰고 나서 반드시 접속끊어야 함. 