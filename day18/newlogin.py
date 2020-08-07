from PyQt5 import QtCore, QtGui, QtWidgets, uic #gui도구 pyqt5
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("e:/login.ui",self) #ui를불러서 실행시켜줘 (읽어와 )
        self.show() #반영됨. 
#변수 잘 적어둬야 안 헷갈림. 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())
#게임계발에 최적화 되어 있는 애 pip install pygame 