
import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton #버튼 만들려고  #작은 윈도우 요소 === 위잿,,, 위잿중에서 from 모듈 import 함수 에풀리케이션과 ,약자를 쓰는 애들은 대문자롤 씀 
from PyQt5.QtCore import QCoreApplication      #만드는 회사에 메뉴얼 보면서 알아가는 것 
class MyApp(QWidget):   #꼭 이렇게 쓸 필요는 없음  #위잿을 상속받았어요, 


    def __init__(self):
        super().__init__()
        self.initiUI()
        #부모 변수 초기화 해야 쓸 수 있음. 
    def print(self):
        print("버튼이 눌림.. 왜 눌러... ^^")
        
 
        
    
        #푸쉬버튼 객체 생성 #
         #UI 담당 함수 User Inerface의 약자 -- > UI 직접 접하는 부분 
#창의 타이틀 지정 
    def initiUI(self):


        btn1 =QPushButton("출력",self) #버튼이 올라가야 할 부모 
        btn1.setText("print")  #버튼에 text를 글자를 set해줘   글자를 수정할 때 
        btn1.resize(100,100) #크기 지정 
        btn1.move(300,200) #화면 어디에 할 건지 지정 
        
        btn1.clicked.connect(self.print)#클릭을 하면 connet는 이벤트랑 연결해주는 애,처리할 이벤트 핸들러를 정의해주면 됨#마우스롤 클릭할거야 #저런 함수랑 연결해줘 (self.print)   
        #종료버튼을 만듦 
        btn2 = QPushButton("EXIT",self)  #버튼 하나 더 만듦 
        btn2.move(500,200)
        btn2.resize(100,100)
    
        btn2.clicked.connect(QCoreApplication.instance().quit)


        self.setWindowTitle("와... 금요일이다... 불금불금")  #.찍어서 하는 것은 거의 있는 것 쓰는 것이 대부분, 특별히 무엇을 만들지 않는한 set 뭔가 지정하는 것 
        self.resize(1200,800) #사이즈 지정 
        self.move(300,400) #움직임 
        #화면에 창을 보여주게 설명
        self.show()

#얘네가 만들어 놓은 인스턴스에 종료   #현재 인스턴스에 응용 위에서 불러와서 쓰는 것 , 현재 창 종료해랄 
        #지정한 거지 실행 안함 

        #메인 포거스 실행은 아냐 

if __name__=="__main__":
    app = QApplication(sys.argv)#실행하려고 
    ex = MyApp()
    sys.exit(app.exec_())
    
#스크롤 하는 것을 이벤트라고 하고 이벤트를 처리하는 애를 이벤트핸들러라고 함, 이벤트는 사건, 창을 가지고 쓸 때 사용하는 모든 사건-- 클릭, 이동 등 
