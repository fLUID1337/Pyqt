from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction
import sys
from PyQt5.QtGui import QPixmap,QIcon
from game import Game
from PyQt5.QtGui import QPixmap

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gamestone\\test1.ui",self)
        self.btn.clicked.connect(self.start)
        self.btn1.clicked.connect(self.start)
        self.show()
    def start(self):
        sender=self.sender()
        self.label.setText(sender.text())
            
            
    
    
    
    
a = QApplication(sys.argv)
d = Main()
sys.exit(a.exec())     