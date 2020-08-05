#lineediter 

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit,QMessageBox#버튼 만들려고  #작은 윈도우 요소 === 위잿,,, 위잿중에서 from 모듈 import 함수 에풀리케이션과 ,약자를 쓰는 애들은 대문자롤 씀 
from PyQt5.QtCore import QCoreApplication      #만드는 회사에 메뉴얼 보면서 알아가는 것 
class MyApp(QWidget):   #꼭 이렇게 쓸 필요는 없음  #위잿을 상속받았어요, 


    def __init__(self):
        super().__init__() #부모의 초기화 함수 부름 ui호출  myapp 
        self.initiUI()#함수 실행해 
        #부모 변수 초기화 해야 쓸 수 있음. 
        #인스턴스으 변수가 되여어야 다른 함수가 될 수 있음, 
    def print(self):
        id = self.leId.text()
        pw =self.lePw.text()
        print(id,type(id))#지정할 때는 setText() =---글자를 지정해주는 것, 가져올 때는 text()
        print(pw,type(pw))
        if id == "aaa" and pw =="bbb": 
            print("로그인 성공")
        else:
            print("로그인 실패")
        self.leId.setText("") #reset
        self.lePw.setText("") #reset되게 하는 것 

            #데이터 베이스에 해서 비교해서 하는 것이 안전함 
        #스트링 타입으로 가져오는 것을 알 수 있음.

        #5입력하고 누르면 5단 7단입력하고 누르면 7단, lineedit
        #문자가 아닌 숫자로 프린트해야 7단 출력 
        #
    #사람안의 쉼터 
    def close(self):
        QMessageBox.question(self, "메세지", "정말 나갈려구",QMessageBox.Yes| QMessageBox.No, QMessageBox.No) #맨 뒤에 있는 것 기본값 
        print("클로즈 함수 호출되고 있음")
        print(response) ##함수만들어서 정말 나갈려구 만듦 
        #처음부터 막아버릴 수도 있음 
        if response == QMessageBox.Yes: #이것의 응답같이 yes와 같으면 
            print("나가지마")
            QCoreApplication.instance().quit() #현재 인스턴스에 나가는 것 호출 
        

    #인턴스에 접근할 수 있게끔  
        #푸쉬버튼 객체 생성 #
         #UI 담당 함수 User Inerface의 약자 -- > UI 직접 접하는 부분 
#창의 타이틀 지정 
    def initiUI(self):
#따로 부를 수 있으니까  따로 부름  # 16348 클로즈 함수 호출되고 있음 --- 다 상수로 만들어서 기억할 수 없는 값
        #label 2개
        labelId = QLabel("ID", self)   #지역변수, 끝나면 사라짐, 함수 밖에서도 접근 해야 self.해서 myapp인스턴스변수되게 함 
        labelPw = QLabel("PW", self)
        #font 크기 글자 
        font1=labelId.font() #폰트객체만들기 
        font1.setPointSize(20) #크기지정함
        labelId.setFont(font1)

        font2=labelPw.font()
        font2.setPointSize(20)
        labelPw.setFont(font1)
        
        labelId.move(300,150)
        labelPw.move(300,250)
        labelId.resize(120,50)
        labelPw.resize(120,50)
    
    #QLineEdit
        self.leId = QLineEdit(self) #인스턴스변수로 만들자
        self.lePw = QLineEdit(self) #인스턴스변수로 만들자  
       
        self.leId.move(500, 150)
        self.lePw.move(500, 250)
        self.leId.resize(120, 50)   #글자를 입력하면 글자가 터미널에 찍히게 하고 싶어요. 
        self.lePw.resize(120,50)
        self.btn1 =QPushButton("출력",self) #버튼이 올라가야 할 부모 
        self.btn1.setText("print")  #버튼에 text를 글자를 set해줘   글자를 수정할 때 
        self.btn1.resize(120,80) #크기 지정 
        self.btn1.move(500,500) #화면 어디에 할 건지 지정 
        
        self.btn1.clicked.connect(self.print)#클릭을 하면 connet는 이벤트랑 연결해주는 애,처리할 이벤트 핸들러를 정의해주면 됨#마우스롤 클릭할거야 #저런 함수랑 연결해줘 (self.print)   
        #종료버튼을 만듦 
        btn2 = QPushButton("EXIT",self)  #버튼 하나 더 만듦 
        btn2.move(700,500)
        btn2.resize(120,50)
    #한줄 수정가능한 lineedit --- 얘도 객체 값을 하나 담을 수 있는 수정가능한 객체 
    # 인스턴스종료하는 함수 
    #     btn2.clicked.connect(QCoreApplication.instance().quit)
        btn2.clicked.connect(self.close) #close 함수에 연결해줘 
#누르면 종료해야줘 너 진짜 종료할 거니 ?  #close 함수 만들고 


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
