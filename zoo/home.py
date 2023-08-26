from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton, QSplitter,QHBoxLayout,QSlider
import sys
from PyQt5.QtGui import QPixmap,QIcon,QColor,QPainter,QFont,QPen,QBrush
import random
from PyQt5.QtCore import Qt

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.setGeometry(250,250,300,100)
        self.sld=QSlider(Qt.Horizontal, self)
        self.text="Привет, я Дима"
        self.sld.valueChanged[int].connect(self.slider)
        self.cor=50
        self.show()
    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        self.drawText(event,qp)
        self.drawBrush(qp)
        qp.end()  
    def drawText(self,event,qp:QPainter):
        qp.setPen(QColor("red")) 
        qp.setFont(QFont("Arial",15))  
        qp.drawText(event.rect(),Qt.AlignCenter,self.text)            
    def drawBrush(self,qp:QPainter):
        pen=QBrush(Qt.Dense5Pattern)
        qp.setBrush(pen)
        qp.drawRect(20,20,self.cor,50)
    def slider(self,value):
        #self.setGeometry(250,250,160 +int((value + (1)) *2 ), 100)
        self.cor+=50
        self.update()

        

                    
        
        
a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())                 
        