import sys 
from PyQt5.QtWidgets import *


#윈도우 를 생성하는 클래스 : QMainWindow, Qwidget, QDialog 3가지로 창을 만듦
#메인윈도우를 생성하기 위한 클래스 QMainWindow, QDialog를 사용해서 생성 
class Mywidget(QWidget): #상속을 받음. 
    def __init__(self) #초기화 변수
        super().__init__()
        self.show #현재창이 보이게 하려면 show 넣어야했음 
#QMainWQindwoL: QHBoxLayout, QVBOxLayout 같은 layout 사용할 수 없다 . 얘는 자체 레이아웃 사용 

#사이에 뭔가 하고 싶은 것 넣음
if __name__ == "__main__"  #이런 이름이 있다면,, name 
#QApplication 클래스의 인스턴스를생성 
print(app.exec_()) #g현재 프로세스 종료해줘 app.exec(0)이면 정상종료 다른 

ex = Mywidget() #애플리케이션 시작, 이벤트 루프에 뭔가에 의해서 종료되면 종료하고 나와라. sys 루프계속 돌다가 종료되면 종료됨. 그 사이., ex = mywidget 그 사이 우리가 만든 위젯이 있는 것 



