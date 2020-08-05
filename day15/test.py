
import sys 
from PyQt5.QtWidgets import *

def quit():
    print("quit() 호출됨")
    sys.exit(0) #0: 정상종료 ,  다른값 비정상 종료 #비정상종료가 더 빨리 끝남/  #g현재 프로세스 종료해줘 app.exec(0)이면 정상종료 다른 
app = QApplication(sys.argv) #Qapplication 클래스의 전달해서 실행해달라는 것 초기화 함수 전달하면서 sys,argv전달하면서 초기화 함수 되는 것 
print(app) #인스턴스 만들어지는 것 볼 수 있음.  #파일 이름 경로 app 경로가지고 파일을 만들어, app, sys.argv  
#대문자 얘네가 만들어 application 인스턴스 만들고 짠 하고 인터프린터이기 때문에 

app.exec_() #끝나지 않고 기다리세요. #이벤트 루프 
#종료되지 않고 반복되고 있음. 종료하지 말고 무한루프만들어 놓은 것 눈에 보이는 것은 없지만 실행중 
btn = QPushbButton("Quit")
btn.show()
btn.clicked.connect(quit)
#사이에 뭔가 하고 싶은 것 넣음
print(app.exec_()) 


# if __name__ == "__main__":
#     app = QApplication(sys.argv)  #Qapplication 클래스의 전달해서 실행해달라는 것 초기화 함수 전달하면서 sys,argv전달하면서 초기화 함수 되는 것 
print(app) #인스턴스 만들어지는 것 볼 수 있음.  #파일 이름 경로 app 경로가지고 파일을 만들어, app, sys.argv  
#대문자 얘네가 만들어 application 인스턴스 만들고 짠 하고 인터프린터이기 때문에 
#     win = MyWindow()
#     sys.exit(app.exec())