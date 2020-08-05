#textEdit : 여러줄 쓸 수 있음
#lineEdit : 한 줄 쓸 수 있음 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *#1. #qtgui는 그림넣는 것 
from PyQt5.QtCore import * 

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.textEdit = QTextEdit() #텍스트 에디터 만듦 
        self.setCentralWidget(self.textEdit)
        self.setWindowTitle("제목없음-windows 메모장")

    
        openFile = QAction(QIcon("./img/notepad.jpg"),"열기", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("파일 열기")
        openFile.triggered.connect(self.showDialog)
        #방아쇠처럼 자동으로 일어나 -- triggered #연결해요, showDialog에

        saveFile = QAction(QIcon("./img/save.png"),"저장",self)
        saveFile.setShortcut("Ctrl+s")
        saveFile.setStatusTip("파일 저장")
        saveFile.triggered.connect(self.saveDialog)

        newFile = QAction(QIcon("./img/openfile.jpg"),"새파일",self)
        newFile.setShortcut("Ctrl+N")
        newFile.setStatusTip("새 파일")
        newFile.triggered.connect(self.newFile)
        
        exitFile = QAction(QIcon("./img/exitfile.jpg"),"끝내기",self)
        exitFile.setShortcut("Ctrl+x")
        exitFile.setStatusTip("종료")
        exitFile.triggered.connect(QCoreApplication.instance().quit)

        #열기에 메뉴바 삽입 
        menubar = self.menuBar() #메뉴바만들어서 
        menubar.setNativeMenuBar(False) #이미지 설정할 거 있냐 없어
        fileMenu = menubar.addMenu("&File") #메뉴바에 추가한다. 
        fileMenu.addAction(openFile)#파일이라는 메뉴에는 오픈파일추가 
        fileMenu.addAction(newFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitFile)

        fontMenu = QAction(QIcon("./img/.png"),"글꼴",self)  #새롭게 서식 만듦  #클릭하면 불러오게 하고 싶어 
        fontMenu.setShortcut("Ctrl+f")
        fontMenu.setStatusTip("글꼴")
        fontMenu.triggered.connect(self.changeFont)

        formMenu=menubar.addMenu("&서식") #폰트 메뉴 붙임 
        formMenu.addAction(fontMenu)

    



        self.setCentralWidget(self.textEdit)#4. 얘는 뭐하는 거지? 
        self.setGeometry(100,100,600,400) 
        self.show() #마지막 
        
    def changeFont(self):
        font, ok = QFontDialog.getFont() #글꼴함수 #선택한 것 맞니? 
        # print("변경 함수 호출")
        if ok:
            self.textEdit.setFont(font)
            #컴포넌트 #이비디드 
    def showDialog(self):#현재 경로 지정해 
        fname = QFileDialog.getOpenFileName(self,'open file',"./") 
        print("show dialog 함수 호출됨")   
        print(fname)#파일 경로 알 수 있음
        
        if fname[0]:
            f = open(fname[0],'r')
            #fname있으면 열고 데이터를 꺼내와
            with f: #with은 자동으로 닫힘
                data = f.read()
                self.textEdit.setText()
#슬레쉬기준으로 끊어서 끝에 것 이름, .으로 구분한 다음 0번째 것만 가져옴
                name = fname[0].split("/" )#fname에 있는 것에서 이름가져와서 잘라온 애들 중에서 앞에 있는애
                print(name[-1].split(".")[0])#리스트니까 0번째 
                self.setWindowTitle("-Windows 메모장")
#이름을 주고 읽어 와요 그리고 textedit에 settext로 넣어둠
    def saveDialog(self):
        # QFileDialog.getSaveFileName#저장할 수 있음
        file = QFileDialog.getSaveFileName(self,"저장","./")
        print(file)
        print(self.textEdit.toPlainText())
        with open(file[0],'w') as f: #이거를 f라고 하고 
            #file[0]은 뭐지? 
            f.write(self.textEdit.toPlainText())#toplaintext는 뭐지?
       #file I/O 
    #저장창 띄워주면 됨. 
    def newFile(self):
        #textEidt에 내용이 있는지를 판단해서 
        txt = self.textEdit.toPlainText()
        print(len(txt))
        #내용이 존재한다면 
        if len(txt) != 0: #응답 
            rep = QMessageBox.question(self,"메모장","변경 내용을 제목 없음에 저장하시겠습니까?",
            QMessageBox.Yes| QMessageBox.No| QMessageBox.Cancel,QMessageBox.Cancel) #cancel이 기본 음영  #매게변수, 뭐컴마, 뭐 컴마 

            if rep == QMessageBox.Yes:
                 self.saveDialog()
                #  file = QFileDialog.getSaveFileName(self,"저장","./")
                #  print(file)
                #  with open(file[0],'w') as f:
                #      f.write(self.textEdit.toPlainText()) #반복되니까 
     

        #저장할 것 인지를 물어보기 저장한 후에 지우기 
        #내용이 없으면 그냥 지우기 
        #to plaintext 글자 가져올 수 있었음, 0이면 없는 것이고 그 외 글자 있음. len(0)저장할거야? 

        
        self.textEdit.setText("")#기존에 있는 텍스트를 초기화
        print("새파일 호출")  
    #새파일열거야, 새파일 기존에 있는 텍스트를 초기화하기만 하면 됨 
    #글자가 있으면 저장할겁니까 묻는 것 나오는 것 


    
#저장된 경로와 이름 나옴. #('E:/dev/python_workspace/text.txt', 'All Files (*)')



if __name__=="__main__": #2. 
    app = QApplication(sys.argv)
    my = MyApp() #현재 객체 생성해 
    sys.exit(app.exec_()) #계속반복해 