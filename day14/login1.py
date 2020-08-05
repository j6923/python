import sys
from PyQt5.QtWidgets import * #qtwidgets는 특정기능을 갖고 있는 애들 window창
from PyQt5.QtCore import *
import cx_Oracle

class myidpw(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.labelId = QLabel("ID",self)
        self.labelPW = QLabel("PW",self)

        self.leId = QLineEdit(self)
        self.lePw = QLineEdit(self)


        self.btnLogin = QPushButton("로그인",self)
        self.btnReg = QPushButton("회원가입",self)
        self.btnLogin.clicked.connect(self.login)
        self.btnReg.clicked.connect(self.register)
        
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)# 여백줌. 
        hbox1.addWidget(self.labelId) #라벨id가 넣음. 
        hbox1.addWidget(self.leId) #라인에디터 넣겠다. 
        hbox1.addStretch(1)
#위젯은 가장 기본적인 애, 메인 윈도우도 상속받고 다른 애도 상속받음. 

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.labelPW)
        hbox2.addWidget(self.lePw)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1) #버튼은 위젯 
        hbox3.addWidget(self.btnLogin)
        hbox3.addWidget(self.btnReg)# 박스3에 login과 회원가입 
        hbox3.addStretch(1)

        vbox = QVBoxLayout() 
        vbox.addLayout(hbox1) #layout을 추가하겠다. 
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        # self.setLayout(hbox)
        self.setLayout(vbox) #최상단에서 vbox를 레이아웃으로 사용하겠다. 
        self.show()
        self.resize(800,600)

    def register(self):
        print("회원가입 버튼 눌림")
        self.nw = MyRegisterWindow(self)
        self.nw.show()
        #사용하려고요 
    def login(self):
        #1. db연결
        connection = cx_Oracle.connect("scott","tigertiger","orcl.cyb0gs2amyei.ap-northeast-2.rds.amazonaws.com:1521/orcl")  #포트:키가 1521번에 맞다. #orcl:db명
        #2. cursor 객체 #connection에 있는 커서를 객체로 만든 것이 커서객체. 
        cur = connection.cursor()  #cur객체를 만들겠다.  앞에 변수명 
        #3. 사용할 sql문 객체 
        sql = '''select id
        from member
        where id= :id, pw= :pw   
        '''
        #4. 실행 
        cur.execute(sql,id=self.leId.text(),pw=self.lePw.text()) #cur가 execute
        cur.execute(sql,[self.leId.text(),self.lePw.text()]) #cur가 execute #text 형식으로 써있음. 라인에디터. text형식 불러오는 애 
        #5. 로직처리 
        for i in cur:
            print(i) 
            if i != None:
                QMessageBox.question(self,"로그인 성공","로그인에 성공하셨습니다.",QMessageBox.Yes,QMessageBox.Yes)
        
        #6. 자원 반납 
        connection.close()

class MyRegisterWindow(QMainWindow):
    def __init__(self,parent): #MyRegisterWindow 매게변수가 있는초기화 함수 호출
        super().__init__(parent) #누르면 창띄우기
        #qmainwindow 띄우려고 
        # 다른 위잿을 포함가능
        self.initUI()#해도 됨

    def initUI(self):
        self.setGeometry(50,50,500,600)
        self.setWindowTitle("회원가입")
        self.lb2Id = QLabel("ID",self) #레이블 두번쨰 id
        self.lb2Id.setGeometry(50,50,100,40)
        self.lb2Pw = QLabel("PW",self) #레이블 두번쨰 id
        self.lb2Pw.setGeometry(50,150,100,40)
        self.lb2Name = QLabel("NAME",self) 
        self.lb2Name.setGeometry(50,250,100,40)

        self.leId = QLineEdit(self)
        self.leId.setGeometry(250,50,100,40)
        self.lePw = QLineEdit(self)
        self.lePw.setGeometry(250,150,100,40)
        self.leName = QLineEdit(self)
        self.leName.setGeometry(250,250,100,40)
        
        self.btn = QPushButton("가입하기",self)
        self.btn.setGeometry(200,350,100,50)
        self.btn.clicked.connect(self.myregister)
        #클릭하면 함수에서 db insert내용이 있으면 됨. 
    def myregister(self):
        print("회원 가입...")

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = myidpw()
    sys.exit(app.exec_())


    #윈도우 레이아웃줘도 안 먹음
    #위젯은 레이아웃주면 먹음. 