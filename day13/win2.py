import sys #시스템 
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton,QLineEdit
class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  #initui 함수를 쓸거예요. 만들거예요  
    def sandan(self):
        for i in range(1,10):
            print("3*",i,"=",3*i)
    def initUI(self): 
        self.setWindowTitle("gugudan")
        self.resize(800,600)
        dan = QPushButton("구구단을 외워요",self) 
        self.QLineEdit("구구단") 
        dan.move(400,300)
        dan.resize(100,100)
        dan.clicked.connect(self.sandan)
        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)#실행하려고 
    ex = myapp()
    sys.exit(app.exec_())
    
#빈칸 lineedit 