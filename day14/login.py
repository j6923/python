import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cx_Oracle
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
#어떻게 배치할까 --- 레이아웃 , 레이아웃하면 MOVE-- 절대 레이아웃 ---> 절대크기의 위치, 딱 고정된 위치갖고 고정됨. 창 크기 변해도 변하지 않음. 
#Lay out >>>> BoxLayout , 상자크기로 수평상자, 수직상자, 로 정렬해서 사용 

    def initUI(self):

        #PyQt에서 이벤트(Signal)처리할 때 사용되는 함수를 이벤트 핸들러(slot)이라고 한다. 시그널에 의해 slot이 작동합니다. 
        
        
        self.labelId = QLabel("ID", self)
        self.labelPw = QLabel("PW", self)      
        


    #QlineEdit #한줄씩 입력받음 
        self.leId = QLineEdit(self)
        self.lePw = QLineEdit(self)


        self.btnLogin = QPushButton("로그인", self)
        self.btnReg = QPushButton("회원가입",self)
        

        hbox1 = QHBoxLayout()#수평상자 레이아웃 객체: 수평을 기준으로   왼쪽에 줌addstrech 위젯 2개 오른쪽에 여백 맨 아래 addstrech1 
        hbox1.addStretch(1) #옆에 공백같이 줌 
        hbox1.addWidget(self.labelId)
        hbox1.addWidget(self.leId)
        hbox1.addStretch(1)


        hbox2 = QHBoxLayout()#수평상자 레이아웃 객체: 수평을 기준으로   왼쪽에 줌addstrecth 위젯 2개 오른쪽에 여백 맨 아래 addstrech1 
        hbox2.addStretch(1) 
        hbox2.addWidget(self.labelPw)
        hbox2.addWidget(self.lePw)
        hbox2.addStretch(1)


        hbox3 = QHBoxLayout()#수평상자 레이아웃 객체: 수평을 기준으로   왼쪽에 줌addstrecthc 위젯 2개 오른쪽에 여백 맨 아래 addstrech1 
        hbox3.addStretch(1) 
        hbox3.addWidget(self.btnLogin)
        hbox3.addWidget(self.btnReg)
        hbox3.addStretch(1)
        vbox = QVBoxLayout() #수직 위아래로 넣음 
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)
        #signal 
        self.btnLogin.clicked.connect(self.dbCheck)#(함수명)
        self.btnReg.clicked.connect(self.register)
#창 타이틀 지정
        self.setWindowTitle("로그인")
#창 사이즈 결정
        self.resize(800,600)
#창 위치 결정 
        self.move(300,400)
# 화면에 보여지게 설정 
        self.show()
    def dbCheck(self):
        print("로그인 버튼 눌림")
#주석만 붙여넣기 해서 공부하기 
    
#1. connecton 객체 생성
        connection = cx_Oracle.connect("scott", "tiger","192.168.0.68:1521/orcl") #db에 연결. 
        print(connection)
#2. cursor 객체
        cur = connection.cursor()


#.3. 사용할 sql문 객체  #문장 길어지면 """ 
        sql = """
        SELECT *  
        FROM member
        WHERE id = :id and pw = :pw
        """
#:변수명 변수라는 명에서 콜론 붙여야 
#4. 실행 
        cur.execute(sql,id=self.leId.text(), pw=self.lePw.text()) #라인에디터에 글자 가져온 것, pw
        #print(cur) #중간중간 잘 되가는지 확인해가면서 하기, 한꺼번에 하려면 오류찾기 어려움 
#5. 로직처리 
        for dbid, pw, name, grade in cur:
            print(dbid, pw)
            if dbid!=None:
                # print("로그인성공") #
                rep = QMessageBox.question(self,"로그인성공","환영합니다", QMessageBox.Yes)

# 6. 자원 반납 
        connection.close()
        #메세지 박스 (성공하면 성공하셨습니다. 띄우기)
        

    def register(self):
        print("회원가입 버튼 눌림")
#현재 파일에서 호출시에만 실행가능하게 설정 

if __name__=="__main__":
    app = QApplication(sys.argv)#실행하려고 
    ex = MyApp() 
    sys.exit(app.exec_())

    #시그널  
    #회원가입해서 가입해서 로그인도 시켜보게 -- 데이터 db에 넣을 수 있어야 