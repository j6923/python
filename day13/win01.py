import sys 
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication
class MyApps(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def print(self):
        print("금요일이다....")


    def initUI(self):

        btn1 = QPushButton("출력",self)
        btn1.setText("이건 뭐지?")
        btn1.resize(100,100)
        btn1.move(0,0)
        # btn2.clicked.connect(self.)
        

        self.setWindowTitle("구구단 3단을 보여줘")
        self.resize(800,600)
        self.move(300,400)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApps()
    sys.exit(app.exec_())
        
