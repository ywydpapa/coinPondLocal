import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog
import dbconn


form_class = uic.loadUiType("./ui/mainWin.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.actionConnect.triggered.connect(self.connectDB)
        self.actionQuit_2.triggered.connect(self.close)
        self.actionSetup.triggered.connect(self.getInfo)


    def btn_clicked(self):
        print("버튼 클릭")

    def connectDB(self):
        print("DB 연결")

    def getInfo(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            print(text)

    def getIncomes(self):
        dbconn.


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainClass()
   app.exec_()
