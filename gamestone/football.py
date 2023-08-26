from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt



class Ball(QWidget):
    def __init__(self,):
        super().__init__()
        self.label=QLabel(self)
        self.x=0
        self.y=0
        self.setGeometry(self.x,self.y,100,100)
        photo_1 = QPixmap("img\\football.png")
        photo_1 = photo_1.scaled(100, 100)
        self.label.setPixmap(photo_1)
        self.game_w=Gates()
        self.game_w.show()
        self.show()
    
    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Down:
            self.y+=20
        if e.key()==Qt.Key_Up:
            self.y-=20
        if e.key()==Qt.Key_Right:
            self.x+=20
        if e.key()==Qt.Key_Left:
            self.x-=20
        self.move(self.x,self.y)
        if self.x == self.y==380:
            self.close()
            self.game_w.close()
             
        
                   

        
        
        
class Gates(QWidget):
    def __init__(self,):
        super().__init__()
        self.label=QLabel(self)
        self.setGeometry(300,300,300,300)
        photo_2 = QPixmap("img\\gates.jpg")
        photo_2 = photo_2.scaled(300, 300)
        self.label.setPixmap(photo_2)
        
        
        
        
        
        
a = QApplication(sys.argv)
d = Ball()
sys.exit(a.exec())             
            