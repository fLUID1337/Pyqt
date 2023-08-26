from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton, QSplitter,QHBoxLayout,QSlider
import sys
from PyQt5.QtGui import QPixmap,QIcon,QColor,QPainter,QFont,QPen,QBrush
import random
from PyQt5.QtCore import Qt

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.setGeometry(300,250,200,150)
        self.text="Привет, я Дима"
        self.show()
    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        self.drawText(event,qp)
        qp.end() 
    def drawText(self,event,qp:QPainter):
        qp.setPen(QColor("red")) 
        qp.setFont(QFont("Arial",15))  
        qp.drawText(event.rect(),Qt.AlignCenter,self.text)
    def drawPoint(self,qp:QPainter):
        qp.setPen(QColor("green"))
        size=self.size()
        for i in range(1500):
            x=random.randint(1,size.width()-1)    
            y=random.randint(1,size.height()-1)
            qp.drawPoint(x,y)  
    def drawPoints(self,qp:QPainter):
        size=self.size() 
        part=size.height()//7
        for num, color in enumerate(("red","orange","yellow","green","light blue","blue","violet")):
            qp.setPen(QColor(color))
            for i in range(10000):
                x=random.randint(1,size.width()-1)
                y=random.randint(part*num,part*(num+1))
                qp.drawPoint(x,y)
    def drawRectangle(self,qp:QPainter):
        spk=[Qt.SolidLine,Qt.DashLine,Qt.DotLine,Qt.DashDotLine]
        coords=[[20,20,150,20],
               [150,20,150,150],
               [150,150,20,150],
               [20,150,20,20]]
        for style,cor in zip(spk,coords):
            pen=QPen(Qt.red,3,style)
            qp.setPen(pen)
            qp.drawLine(*cor)
            
    def drawBrush(self,qp:QPainter):
        spk=[Qt.Dense1Pattern,Qt.HorPattern,Qt.DiagCrossPattern,Qt.BDiagPattern]
        coords=[[20,20,50,50],
               [80,20,50,50],
               [20,80,50,50],
               [80,80,50,50]]
        for style,cor in zip(spk,coords):
            pen=QBrush(style)
            qp.setBrush(pen)
            qp.drawRect(*cor)    
                    
                       





a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())                 
