import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget): #얘를 상속받은 클래스 됨, 나도 위잿이 될 수 있음. 
    def __init__(self):
        super().__init__() 
        self.drawType =1 #1직선 2. 사각형나오게 하고 싶어요. 
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


        self.rbtnLine = QRadioButton("직선",self) #이름이 있어야 되니까 지정해줌 
        self.rbtnCurve = QRadioButton("곡선",self)
        self.rbtnRect = QRadioButton("사각형",self)
        self.rbtnELLipse = QRadioButton("타원",self)
        
        # box1.addWidget(self.rbtnLine) #위젯 넣어줄 수 있음 qradio  #라이오는 한개만 체크, 체크박스는 여러개 가능 
        # box1.addWidget(self.rbtnRect) #위젯 넣어줄 수 있음 qradio 
        # box1.addWidget(self.rbtnCurve) #위젯 넣어줄 수 있음 qradio 
        # box1.addWidget(self.rbtnELLipse) #위젯 넣어줄 수 있음 qradio 

#배경색 붙어넣으면 clear --- 다 지우는 것 하려면 
#지우개 사각형해서 흰색으로 하면 됨. ---사각형 그려서 흰색으로 칠함. 
        box1.addWidget(self.rbtnLine) #위젯 넣어줄 수 있음 qradio  #라이오는 한개만 체크, 체크박스는 여러개 가능 
        box1.addWidget(self.rbtnRect) #위젯 넣어줄 수 있음 qradio 
        box1.addWidget(self.rbtnCurve) #위젯 넣어줄 수 있음 qradio 
        box1.addWidget(self.rbtnELLipse) #위젯 넣어줄 수 있음 qradio 

        self.rbtnLine.clicked.connect(self.radioBtnClicked) #rbtnLine(선)에 클릭하는 시그널이 오면 처리하기 위해 rado호출 , 함수호출한다. 
        self.rbtnCurve.clicked.connect(self.radioBtnClicked) #rbtnCurve(곡선)에 클릭하는 시그널이 오면 처리하기 위해 rado호출 , 함수호출한다. 
        self.rbtnRect.clicked.connect(self.radioBtnClicked) #rbtnRect(사각형)에 클릭하는 시그널이 오면 처리하기 위해 rado호출 , 함수호출한다. 
        self.rbtnELLipse.clicked.connect(self.radioBtnClicked) #rbtnELLipse(타원)클릭하는 시그널이 오면 처리하기 위해 rado호출 , 함수호출한다. 
        #
        self.rbtnLine.setChecked(True)  #버튼에 체크하는 애가 setchecked 그리고 true면 버튼에 기본적으로 체크한 애 . 
        
        self.drawType = 1                #기본값으로 직선가지라고 함. 
 

        self.rbtnLine.setChecked(True) #있어야 하나? 
       #전체 크기 레이아웃 leftbox right box 
        #그룹박스 2 
        gb2 = QGroupBox("Pen setting")   #그룹박스를 만들고 pen setting이 나오게 한다. 
        leftbox.addWidget(gb2) #그룹박스 2번째     #왼쪽박스를 만들고 위젯을 gb2에 실행? 

        grid = QGridLayout() #grid적용, 격자로 
        gb2.setLayout(grid)   #gb2를 대상으로 layout을 지정해(set은 뭔가를 지정하는 것을 말함.grid를 지정해 
                                #gb2를 대상으로 layout을 지정하는데 격자(grid)로 지정해.
 
        gb4 = QGroupBox("FILE")   #함수로 그룹박스를 만들고 "FILE"이 나오게 한다. 
        leftbox.addWidget(gb4)    #왼쪽 박스를 만들고 위젯을 적용시킨다. gb4에 

        hbox4 = QHBoxLayout()     #hbox4에 수평박스를 대입한다.(적용시킨다) 
        gb4.setLayout(hbox4)      ##gb4를 대상으로 layout을 지정하는데 hbox로 지정해. 

        saveBtn = QPushButton("버튼",self)    #버튼을 만들고 "버튼"이라는 글자가 나오게 한다. 그리고 self자기 자신을 받는다. 왜? 
        hbox4.addWidget(saveBtn)               #hbox4에 위젯을 적용시키고 save(Btn)을 실행? 
        saveBtn.clicked.connect(self.save_img) #savebtn을 클릭하면 save_img에 연결시킨다. 

  
        


        frmbox.addLayout(leftbox) #frmbox에 addlayout을 하고 leftbox를 
        frmbox.addLayout(rightbox) #현재 창에  수직박스 두개 얻어놓은 것 

        label = QLabel("선굵기") #레이블 만들어줌 
        grid.addWidget(label,0,0) #모르겠으면 하나씩 늘려보기 #앞은 행, 뒤는 열 #여러개중 하나고르려고요 -- 콤보박스 ,,, 어떤애는 스피너 

        self.combo = QComboBox()  #콤보박스 만듦 #Qcombobox를 만든다. self.combo에 적용 ,왜 self? 
        grid.addWidget(self.combo,0,1)  #grid를 위젯에 적용시키고 combo를 0,1로 한다. ??? 

        for i in range(1,21):
            self.combo.addItem(str(i)) #20가지 선택할 수 있도록 함.

        label2 = QLabel("선색") #선색깔 선택
        grid.addWidget(label2,1,0)  #0번째 1번째 행번호, 열번호 
        self.pencolor = QColor(0,0,0) #rgb값 줄 수 있음 
        self.penbtn = QPushButton() #버튼을 만든다. self.penbtn에 적용시킨다. 
        self.penbtn.setStyleSheet("background-color:rgb(0,0,0)") #css형태로 줄 수 있음, tested syle 시트 ,, 백그라운드 칼라를 rgb,,
        #검은애 #위읭 것 바뀐 색깔로 하고 싶어요. 
        grid.addWidget(self.penbtn,1,1)    
        #선 색상선택 버튼 누르면 색상 고를 수 있는 것 
        self.penbtn.clicked.connect(self.selectColorDig)
        #그룹박스 3
        #부 설정
        gb3 = QGroupBox("붓 설정")   #그룹박스를 만들고 "붓 설정"이 들어가게 한다, 그것을 gb3에 대입한다. 
        leftbox.addWidget(gb3)     #gb3에 우측 박스 위젯을 적용한다. 

        hbox = QHBoxLayout() #수평박스 레이아웃 씀
        gb3.setLayout(hbox)  #gb3에 레이아웃을 적용시킨다???????? 

        label3 = QLabel("붓색상")  #붓색상이라는 글자가 자리를 차지함
        hbox.addWidget(label3)     #

        self.brushcolor = QColor(255,255,255) #빛의 삼원색 레드 그린 블루 0-255 색깔 커질수록 그 색 강해짐. 줄여서 rgb칼라라고 함.
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet("background-color:rgb(255,255,255)")
        hbox.addWidget(self.brushbtn) 

        #붓색상 버튼을 누르면 selectcolordig() 함수를 호출해. 
        self.brushbtn.clicked.connect(self.selectColorDig)
    

        # 우측 레이아웃 박스에 그래픽 뷰 추가 

        self.view = CGView(self) #그래픽 뷰 상속해서 만들거예요. #위에 
        rightbox.addWidget(self.view) #밑에 만든 위젯 
        self.show()

    # def selectColorDig(self):
    #     #색상 대화상자 생성 
    #     print("색 선택 버튼 눌림...")
    #     color = QColorDialog.getColor()  #rgb쓰면 값 나옴. 
    #     #pyqt.gtcui.qcolor object 칼라 놔왔다 볼 수 있음
    def save_img(self):
          #print(self.view.grab(self,view.setSceneRect().toRect()))
        img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
        #   img =self.view.grab(self.view.setSceneRect().torect()) 
        #   print(img)
        #파일선택해서 이 이미지를 저장할수 있을까요? 
        fname = QFileDialog.getSaveFileName(self,"어따가 저장할래?","./")
        print(fname)
        if fname[0]:
            img.save(fname[0])

        # img.save('e:/data.png')  #png로 저장됨. 




    def selectColorDig(self):
         #색상 대화상자 생성 
        color = QColorDialog.getColor()  #보기
        who = self.sender() #눌렀던 애가 누군지 알아낸 다음 
        if who == self.penbtn: #팬 버튼이면 지금 지정한 애 담음 
            self.pencolor=color
            self.penbtn.setStyleSheet("background-color:{}".format(color.name()))
            
            #print("펜 버튼이었어")
        elif who == self.brushbtn:  #팬 컬러인지 브러쉬 컬러인지 봄. 
            self.brushcolor = color  
            self.brushbtn.setStyleSheet("background-color:{}".format(color.name()))  
        #함수의 지역변수되면서 끝나서 
            print("붓 색상 버튼이었어")
        print(self.sender())  #sender로 주소를 알려줌???  
        print(color)     #색깔을 출력한다. 
        print(color.toRgb())   #toRgb는 뭐지?? 
    def radioBtnClicked(self):   #라디오 버튼이 클릭되는 함수를 만든다. 
        print("사각형 라디오 버튼 클릭됨")  #"사각형 라디오 버튼 클릭됨"이 출력되게 한다.   
        #어떤 라디오 버튼이 선택된 것인지 판단
        if self.rbtnLine.isChecked(): #선이 버튼이 선택되었다면 
            self.drawType = 1   #drawType은 1
        elif self.rbtnRect.isChecked(): #사각형이 이 버튼이 선택되었다면 
            self.drawType =2       #drawType은 2
        elif self.rbtnCurve.isChecked():  #곡선이 버튼이 선택되었다면 
            self.drawType = 3       #drawType은 3 
        elif self.rbtnELLipse.isChecked(): #타원 버튼이 선택되었다면 
            self.drawType = 4            #drawType은 4
        print("선택한 타입은:", self.drawType)   #"선택한 타입은:"과 drawType뭐 선택했는지 출력 
   
        #펜하고 붓하고 주소가 달라요. sender로 하면 이 값은 나는 몰라도 컴퓨터알아 ㅑ
#QGraphics 는 시각적 객체의 복잡한 장면을 쉽게 처리 
# 할 수 있는 프레임 워크로 구성하는데 사용할 수 있다. 

#QGrahpicsView, QGraphicsScne, QGraphicsItems

class CGView(QGraphicsView): #그래픽뷰상속 ..그래픽 scene이란 걸 사용, 원활하게 제어하게 해주기위한 것이 graphicsview
    def __init__(self,parent):
        super().__init__(parent)  #부모창입력하면 부모 초기화함수 호춣하면서 됨
        self.scene = QGraphicsScene() #아이템 시작위치 등 몇 개 변수 초기화됨. 이게 뭐였더라?  
        self.setScene(self.scene)     #
 #cgv에 부모창에 대한 인자 parent전달 되고 있음
        self.items = []
        self.start = QPointF() #F은 실수 값있는 것 , F없는 것은 정수값.. 시작점  
        self.end = QPointF()#끝점 좌표  이걸로 초기화, 위쪽에 self=cgview초기화해,, 그래서 self.view로 붙임. 

    def moveEvent(self,e):
        rect = QRectF(self.rect())#창사이즈 절대 커지지 않게 줌 #움직임은주지만 지우게 땔때만 그리게 
        rect.adjust(0,0,-3,-3) #원 사이즈에서 이 크기에 약간 작게 만듦. 00은 시작점. 
        
        self.scene.setSceneRect(rect) #신의 크기가 창에 맞게 작게 되서 창밖으로 벗어나지 않게 됨 
        #print("moveEvent 호출됨") #뭐하는애인지 알 수 있도록 찍어봄 #창 움직일 떄 

    def mousePressEvent(self,e):#마우스 누를 때 시작점 끝점 필요, 초기화하자 
        if e.button()  == Qt.LeftButton: #1: #왼쪽버튼 클릭하면 1번은 왼쪽, 2번은 오론쪽  #영어철자로 값만 갖고 있는 변수로 안 그러면 못 알 아봄 만약 
            #이벤트 일어난 버튼이 왼똑버튼이면 숫자나 1,2,안 쓰고 숫자값 대신 할 수 있는 변수 가져오는 것이 프로그래머 추세 
        #e에 이벤트라는 뜻 이벤트일어나면 호출 , 이벤트의 정보가 옴, 
        #print("마우스 클릭됨")
            self.start = e.pos() #좌표값을 시작 종료에 담아놓음 
            self.end =e.pos()
            #print(e.pos()) 좌표값 들어있겠네. 클릭하고 마우스 움직이면 이벤트 일어남, 그 좌표점을 end의 좌표점으로 삼아볼게요. 
        #시작점 저장   
        #클릭하고 릴리지할 때마다 이벤트 다시 잡아줘 이런 모양이 나옴. 흔들림, 채우기 위해서 사이즈 늘려남, 그래서 흔들림

    
    def mouseMoveEvent(self,e): #sence이 일종의 도화지 
        
        self.end = e.pos() #포지션을 self.end로 삼음.  #마우스 드래그 할 때 
        pen = QPen(self.parent().pencolor,self.parent().combo.currentIndex()+1)
        #pen = QPen(QColor(Qt.red),self.parent().combo.currentIndex())#기본값, 검정색 칼라와 사이즈 줄 수 있음     #빨간색, 5인 펜을 준비#색깔, 사이즈 
        #콤보박스에 몇번째것 갖고 오면 됨. 그러면선택 가능 
        #현재 선을 추가 
    
        
#scene에 그려진 이전 선을 제거 
        #self.items 선들을 다 넣을 것,그리고 여기있는 것 지워버림.  

        line = QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
       # line = QLineF(시작x,시작y,종료x,종료y)  
        # self.scene.addLine(line,pen)1
        #self.items.append.self.scene.addLine(line,pen) #라인그리는 애를 그리고 append시켜요. 2 
        #self.scene.addLine(라인객체, 펜종류) #라인추가
        if len(self.items)>0: #0이 아니면 지움 
            self.scene.removeItem(self.items[-1]) #마지막것 하나 뺴고 지워줘    
            del(self.items[-1])  #뭐였더라? 

        
        if self.parent().drawType == 1:        #왜 왔지? 다시 
            line=QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
            self.items.append(self.scene.addLine(line,pen))
        elif self.parent().drawType ==2:
            
        # print(self.items)
    #     print("마우스가 드래그 됨")
#시작점 끝점 동일함  --- 직선과 사각형 
        #사각형 그리기 
            brush = QBrush(self.parent().brushcolor)  #붓을 부모가 지정한 붓색깔로 하고 brush에 대입한다. ##맞나? 
            # brush = QBrush(QColor(200,100,200))
            rect = QRectF(self.start,self.end) #사각형의 플로타입, X,Y좌표 가짐.    #rect에 사각형의 x와 y좌표를    해석 
            self.items.append(self.scene.addRect(rect,pen,brush))    #해석. 
        # print(self.items)

        #곡선그리기 
        elif self.parent().drawType ==3:   #if else 부모의 drawtype이 3이면 
            line = QLineF(self.start.x(),self.start.y(), self.end.x(), self.end.y()) #
            self.scene.addLine(line,pen)
            self.start = e.pos()
        elif self.parent().drawType ==4:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start, self.end)
            self.items.append(self.scene.addEllipse(rect,pen,brush))
    def mouseReleaseEvent(self,e): #마우스 떼는 것을 release라고 함.
        self.end = e.pos()
        pen = QPen(self.parent().pencolor,self.parent().combo.currentIndex()+1)
        if self.parent().drawType == 1:
            line=QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
            # pen=QPen()
            self.scene.addLine(line,pen)
        elif self.parent().drawType ==2:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start,self.end)
            self.scene.addRect(rect,pen,brush)
        elif self.parent().drawType ==4:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start, self.end)
            self.scene.addEllipse(rect,pen,brush)
        
    
            
        #print("마우스를 땔 때")
        # self.end = e.pos() #포지션을 self.end로 삼음.  #마우스 드래그 할 때   #moved다 그리니까 이상한 move할 때마다 앞의것 지우고 새로그리고 하면 움직이는 지점에서 볼 수 
        # #있음, 딱 때면 그것만 그리게 
        # pen = QPen()#기본값    #빨간색, 5인 펜을 준비#색깔, 사이즈 
        
        #line = QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y()) #직선을 그려요 
       
        #self.scene.addLine(line,pen)
            # brush = QBrush(QColor(200,100,200))
            
            # rect = QRectF(self.start,self.end) #사각형의 플로타입, X,Y좌표 가짐. 
            # self.items.append(self.scene.addRect(rect,pen,brush))##???? 에러남. 
        print(self.items)
    
    #움직임 제어하는 게 들어있음 
    #paint 위젯에 있던것 

if __name__ == "__main__":
    app = QApplication(sys.argv) #초기화함수해서 
    m = MyApp() #얘를 만들어  #초기화해서 만들어 
    sys.exit(app.exec_())  #메인 루프 

#같은 함수이기 때문에 누가 나를 불러는지 알아낼 필요 있음 
