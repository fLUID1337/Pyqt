from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton, QSplitter,QHBoxLayout,QSlider
import sys
from PyQt5.QtGui import QPixmap,QIcon,QPainter,QFont,QColor
import random
from PyQt5.QtCore import Qt

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.text="Привет, я Дима!"
        self.setGeometry(250,250,300,1000)
        self.sld=QSlider(Qt.Horizontal, self)
        self.sld.valueChanged[int].connect(self.slider)
        self.show()
    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        self.drowText(event,qp)
        qp.end()   
    def drowText(self,event,qp:QPainter):
        qp.setPen(QColor("red")) 
        qp.setFont(QFont("Arial",15))  
        qp.drawText(event.rect(),Qt.AlignCenter,self.text)     
    def slider(self,value):
        self.setGeometry(250,250,160 +int((value + (1)) *2 ), 1000)
        self.text+="\nПривет,я Дима! Приятно познакомиться"
        
        
        





a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())                 
