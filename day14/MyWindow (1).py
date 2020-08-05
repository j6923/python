import sys

from PyQt5 import *
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import time
class MyWindow2(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("메롱~~~~")
        p_img = QPixmap("peach.png")
        self.lb = QLabel("메롱", self)
        self.lb.setPixmap(p_img)
        self.lb.setGeometry(0,0,200,200)
        self.show()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("나의윈도우")
        # self.move(200,200)
        # self.resize(300,300)
        self.setGeometry(200,200,300,300)
        self.btn = QPushButton("Click me ", self)
        self.btn.move(100,100)
        self.btn.setToolTip("<h3>날 눌러봐!!</h3>")
        self.btn.clicked.connect(self.newWindow)
        self.show()

    def newWindow(self):
        for i in range(10):
            time.sleep(0.2)
            # self.nw = QMainWindow(self)
            self.nw = MyWindow2(self)
            self.nw.move(100+i*100,100)
            self.nw.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec())