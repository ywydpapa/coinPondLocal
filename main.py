import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import dbconn


form_class = uic.loadUiType("./ui/mainWin.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.saveBtn.clicked.connect(self.btn_clicked)


    def btn_clicked(self):
        print("버튼 클릭")


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainClass()
   app.exec_()
