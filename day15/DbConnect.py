import cx_Oracle
from DbConnect import Dbconnect #

class DbConnect:
    def __init__(self,host,dbname, user, password, port=1521):
        self.host = host
        self.port = port #반복되는 부분이 있어 클래스를 지정하고 쓰면 길게 6개문장 안 써도 쓸 수 가 있음. 
        self.user = user
        self.password = password  #self, user 등 self.connection에 전달되는 애들을 써준 것 변수를 받아서 전달해야 하니까. 
        self.dbname =dbname
        self.connection = cx_Oracle.connect(self.user,self.password,self.host+":"+self.port+"/"+self.dbname) #self.host+":" 문자열 넣어줌 
        print(self.connection)  #"192.168.0.68:1521/orcl"써주기 위해서 ":"와 self.port+"/"넣어줌. 
#다 안 쓰고 짧게 해서 db연결 가능 

    def execute(self,sql): #sql문 받아줌 
        self.connection.cursor #connection에서 커서만들어야함. 현재컨넥스에서 커서 만듬 
        #이 커서로 이스큐트 sql문장 실행 
        # 데이터 
        cur =self.connection.cursor() #데이터 집함 리저트셋, 가리켜주는것을 cursor라고함. 
        cur.execute(sql)
        resultList = [] #반복해서 하나씩 추가하고 여기에 넣음. 
        for x in cur:
            resultList.append(x)
        self.connction.close()
        
        return resultList
if __name__ =="__main__":  #메인일때만 실행하려고 

    db = DbConnect("192.168.0.68", "orcl", "scott", "tiger", "1521")
    print(db.execute("SELECT * FROM dept"))