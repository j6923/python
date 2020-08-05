import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton  #여기추가 QPushButton #모듈 밑에 또 다른 모듈을 가지고 있어요.  #불러옴.
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
class MyApp(QWidget) : 
    #나도 위잿이 됨

    def __init__(self):
        super().__init__()
        self.initUI() #유아이화면 구성할 거예요. 이런 이름의 함수를 호출해 
    
    def initUI(self):
        btn = QPushButton("나가기", self)   #버튼을 생성 
        btn.move(100,100) #버튼은 위치를 100,100옮김
        btn.resize(500,500) #버튼의 크기를 
        
        btn.clicked.connect(QCoreApplication.instance().quit) #바인딩 #버튼을 클릭하면 연결해주세요 여디에 
        
        self.setWindowTitle("내가 만든 윈도우창") #그 이름으로 그 자리에 들어감. 
        self.move(10,10)   #얘 뭐지? 
        self.setWindowIcon(QIcon("./img/instagram.png")) #생성해줌. 아이콘을 만들려고QIcon +파일 이미지 #.밑에 이미지 
        
        # self.show() #이 창이 보여지게 
        self.resize(1200,600) #uI에 관련된 거는 여기에서 
        self.show()
if __name__=="__main__":  
    app = QApplication(sys.argv)
    ex = MyApp()   #얘네는 왜 써? 
    sys.exit(app.exec_())
    
    #똑같이 리눅스 유닉스에 띄우면 거기에 맞게 됨. 

    #아이콘 바꾸고 싶습니다. 

