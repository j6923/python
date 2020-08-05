#내가 만든것 별도의 window 
#자체 내장 import하면 되는데 그 중 특정기능 쓰고 싶으면 외부에 있는 라이브러리 가지고 오면 됨. 

#너 지금 쓰고 있는 패키지가 버전이 좀 낮아. 
#새로운 것에 대한 링크는 
#그때 지금 버전 20.1.1 버전인데 20.2 최근에 추가되는 것 받을 수 있어, 업데이트 해보는 게 어떄? 나중에 갱신된 버전을 쓸 수 있어, 그래서 한번쯤 실행해주는 것이 좋아. 

#안해도 되지만 === python.exe 

#pip install 패키지명 --- > 터미널 창에 
#c## 

#window창 만들기 

import sys 
from PyQt5.QtWidgets import QApplication,QWidget   #모듈 밑에 또 다른 모듈을 가지고 있어요.  #불러옴.
from PyQt5.QtGui import QIcon
class MyApp(QWidget) : 
    #나도 위잿이 됨

    def __init__(self):
        super().__init__()
        self.initUI() #유아이화면 구성할 거예요. 이런 이름의 함수를 호출해 
    
    def initUI(self):
        self.setWindowTitle("내가 만든 윈도우창") #그 이름으로 그 자리에 들어감. 
        self.move(10,10)   
        self.setWindowIcon(QIcon("./img/instagram.png")) #생성해줌. 아이콘을 만들려고QIcon +파일 이미지 #.밑에 이미지 

        # self.show() #이 창이 보여지게 
        self.resize(1200,600) #uI에 관련된 거는 여기에서 
        self.show()
if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
    #똑같이 리눅스 유닉스에 띄우면 거기에 맞게 됨. 

    #아이콘 바꾸고 싶습니다. 

