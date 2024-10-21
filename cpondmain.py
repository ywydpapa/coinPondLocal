import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


form_class = uic.loadUiType("./ui/mainWin.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainClass()
   app.exec_()
