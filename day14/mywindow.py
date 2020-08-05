import sys   #가져옴.  

from PyQt5 import *     
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import * #그림나오게 하는 외부 
import time  
#부모없으면 none해서 내가 쓸게 parent 어느 창 밑에 붙어있어, 클래스 가능 
class Mywindow2(QMainWindow): #class 만듦  qMainwindwo를 상속받게 
    def __init__(self,parent):  #부모에게 전달하는 것 parent ,매게 변수 self주고 다른 하나 더 줄 수 있음. parent부모창이 누구니?
        super().__init__(parent) #super는 부모 매게변수 가진애가 있어요? 있으니까 씀, 없으면 부모없으면 none의 상태 #mywindow2주면서 self로 받아줌.
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("메롱~~~~~") 
        p_img = QPixmap("./img/peach.jpeg") #그림을 지정해줌. 
        self.lb = QLabel("메롱", self)  #네임달 수있있음 
        self.lb.setPixmap(p_img) #
        self.lb.setGeometry(0,0,200,200) #레이블 위치지정 
        self.show()
#(self, data =None)있으면 받고 없으면 none 매게변수에 초기값줄 수 있어요, 지정하지 않아도 초기값 줄 수 있어, 안 주면 안받어. 
class MyWindow(QMainWindow):    #class 만듦,Qmainwindow의 것을 상속받음     
    def __init__(self):          #초기화함.  
        super().__init__()       #부모것도 초기화, 상속받음 
        
        self.setWindowTitle("취업지원") #윈도우 위에 줄에 "나의윈도우"라고 타이틀함
        # self.move(200,200)                   #좌표 200,300으로 이동
        # self.resize(300,300)                 #크기를 300,300으로 함
        self.setGeometry(200,200,300,300) #move xy너비,높이 를 위의 2ㄷ개를 한줄에 쓸 수 있는 함수 
        self.btn = QPushButton("비법자소서보기", self) #버튼을 만들었음.
        self.btn.move(100,100)                 #버튼을 이동시킴 100,100
        self.btn.setToolTip("<h3>날 눌러봐!</h3>") #마우스 갖대댜면 tool  #? 갖다대면 문구가 나오게 함. 
        #html 태그 넣을 수 있음
        #마우스 갖다대면 풍선되는 
        self.btn.clicked.connect(self.newWindow) #클릭할 때 newindwow로 연결--- > signal이라고 했고 처리하는 것을 핸들...
        #창이 여러개 뜨게 함.     #self는 부모여서 씀. 
        self.show()  #보이게 함. 내 창 보이게 함 
    

    def newWindow(self):   #newWindow 함수 만듦
        for i in range(10):        #10번 뜨게 함. 
            time.sleep(0.2) #0.2초씩 간격으로 잠들어.  
            self.nw = Mywindow2(self) #QMainWindow(self)를 상속받음 
            # self.nw = QMainWindow(self)  #새창띄움, 빈 윈도우 창, self실행하고 있는 창에 빈 윈도우 하나 더 띄움 
            #라벨이 나오게 함. 
            
            self.nw.move(100+i*100,100) #옆으로 뿅뿅 나오게끔  +i 도배기능이 얘의 기능을 가지고 있지만 주석처림 상속받은 mywindow 커스텀 윈도우창 
            #겨비기 않게, 100에서 한개씩 이동할 때마다 i 
            self.nw.show() #윈도우 창 뜨게  
        #self.hide()  #자기 창은 꺼지게 #메인이 살아있어야 함. 
        #실행파일로 만들기 
            
        
        #파이션없더라도 실행될 수 있도록 
        #pip installer c



if __name__ == "__main__": #여기서만 실행되게 하기.   
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec())         

#상속받은 mywindow class :
