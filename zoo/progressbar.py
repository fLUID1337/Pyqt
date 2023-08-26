from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton, QSplitter,QHBoxLayout,QProgressBar
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt,QBasicTimer


class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.btn=QPushButton(self)
        self.btn.setGeometry(100,100,150,50)
        self.btn.setText("Start")
        self.pbar=QProgressBar(self)
        self.btn.clicked.connect(self.changeValue)
        self.timer=QBasicTimer()
        self.step=0
        self.show()
    def changeValue(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("Start")
        else:
            self.timer.start(100,self)
            self.btn.setText("Stop")
    def timerEvent(self,e):
        if self.step>=100:
            self.timer.stop()
            self.btn.setText("Finished")
            return
        self.step+=5
        self.pbar.setValue(self.step)       
                
        
            



a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())             