import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget): #얘를 상속받은 클래스 됨, 나도 위잿이 될 수 있음. 
    def __init__(self):
        super().__init__()
        self.initUI() #initUI실행해 해서 밑에 만듦 
    def initUI(self):  #Ui관련된것 
        self.setGeometry(100,100,1000,800) #xy너비높이 
        #전체 폼  #전체 레이아웃은 폼 박스로 가져옴. 전체 수평폼 레이아웃 
        frmbox = QHBoxLayout() #수평박스 레이아웃 쓸거예요
        self.setLayout(frmbox) #수평박스 레이아웃 적용해줘 

        #좌측 레이아웃
        leftbox = QVBoxLayout() #좌측 우측 박스 만들음 
        rightbox = QVBoxLayout()
        

        
        #좌측 레이아웃 메뉴같은 넣어보기 
        
        gb = QGroupBox("타입") #그룹박스 만들고  전체 창안에 밑줄같은 --- groupbox  #안에 레이아웃 몇 개하면 관리하기 쉽고 보기쉬움
        leftbox.addWidget(gb) #이 위젯을 붙여줘, 
        box1 = QVBoxLayout()  
        gb.setLayout(box1)

        box1.addWidget(QRadioButton("직선",self)) #위젯 넣어줄 수 있음 qradio  #라이오는 한개만 체크, 체크박스는 여러개 가능 
        box1.addWidget(QRadioButton("곡선",self)) #위젯 넣어줄 수 있음 qradio 
        box1.addWidget(QRadioButton("사각형",self)) #위젯 넣어줄 수 있음 qradio 
        box1.addWidget(QRadioButton("타원",self)) #위젯 넣어줄 수 있음 qradio 

       
        #그룹박스 2 
        gb2 = QGroupBox("Pen setting")
        leftbox.addWidget(gb2) #그룹박스 2번째 

        grid = QGridLayout() #grid적용, 격자로 
        gb2.setLayout(grid)
    

        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox) #현재 창에  수직박스 두개 얻어놓은 것 

        label = QLabel("선굵기") #레이블 만들어줌 
        grid.addWidget(label,0,0) #모르겠으면 하나씩 늘려보기 #앞은 행, 뒤는 열 #여러개중 하나고르려고요 -- 콤보박스 ,,, 어떤애는 스피너 

        combo = QComboBox()  #콤보박스 만듦 
        grid.addWidget(combo,0,1)

        for i in range(1,21):
            combo.addItem(str(i)) #20가지 선택할 수 있도록 함.

        label2 = QLabel("선색") #선색깔 선택
        grid.addWidget(label2,1,0)  #0번째 1번째 행번호, 열번호 
        self.pencolor = QColor(0,0,0) #rgb값 줄 수 있음 
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet("background-color:rgb(0,0,0)") #css형태로 줄 수 있음, tested syle 시트 ,, 백그라운드 칼라를 rgb,,
        #검은애 
        grid.addWidget(self.penbtn,1,1)
    

        #그룹박스 3
        #부 설정
        gb3 = QGroupBox("붓 설정")
        leftbox.addWidget(gb3)

        hbox = QHBoxLayout() #수평박스 레이아웃 씀
        gb3.setLayout(hbox)

        label3 = QLabel("붓색상")  #붓색상이라는 글자가 자리를 차지함
        hbox.addWidget(label3)

        self.brushcolor = QColor(255,255,255) #빛의 삼원색 레드 그린 블루 0-255 색깔 커질수록 그 색 강해짐. 줄여서 rgb칼라라고 함.
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet("background-color:rgb(255,255,255)")
        hbox.addWidget(self.brushbtn) 
        # 우측 레이아웃 박스에 그래픽 뷰 추가 

        self.view = CGView(self) #그래픽 뷰 상속해서 만들거예요. 
        rightbox.addWidget(self.view) #밑에 만든 위젯 
        self.show()
#QGraphics 는 시각적 객체의 복잡한 장면을 쉽게 처리 
# 할 수 있는 프레임 워크로 구성하는데 사용할 수 있다. 

#QGrahpicsView, QGraphicsScne, QGraphicsItems

class CGView(QGraphicsView):
    def __init__(self,parent):
        super().__init__(parent)  #부모창입력하면 부모 초기화함수 호춣하면서 됨
        self.scene = QGraphicsScene() #아이템 시작위치 등 몇 개 변수 초기화됨. 
        self.setScene(self.scene)

        self.items = []
        self.start = QPointF()
        self.end = QPointF()



if __name__ == "__main__":
    app = QApplication(sys.argv) #초기화함수해서 
    m = MyApp() #얘를 만들어  #초기화해서 만들어 
    sys.exit(app.exec_())  #메인 루프 