from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton, QSplitter,QHBoxLayout,QCheckBox
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.cb_1=QCheckBox("Разблокировать",self)
        self.cb_2=QCheckBox("Нажми на меня",self)
        self.setGeometry(100,100,100,100)
        self.cb_2.move(0,20)
        self.cb_2.stateChanged.connect(self.btn_2)
        self.cb_1.stateChanged.connect(self.btn_1)
        self.cb_2.setEnabled(False) 
        self.show()
    def btn_2(self,state):
        if state==Qt.Checked:
            self.setWindowTitle("Нажато")
        else:
            self.setWindowTitle("Не нажато")
    def btn_1(self,state):
        if state==Qt.Checked:
            self.cb_2.setEnabled(True)
        else:
            self.cb_2.setEnabled(False)            
                    




a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())         