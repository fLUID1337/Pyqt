from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction
import sys
from PyQt5.QtGui import QPixmap,QIcon
from game import Game
from PyQt5.QtGui import QPixmap

class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("gamestone\\main.ui",self)
        self.btn.clicked.connect(self.start)
        self.show()
    def start(self):
        count_stone=self.spin.value()
        self.game_w=Game(count_stone)
        self.game_w.show()
        self.close()      
            
    
    
    
    
a = QApplication(sys.argv)
d = Main()
sys.exit(a.exec())     