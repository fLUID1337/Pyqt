from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton,QFontDialog
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt





class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.btn=QPushButton(self)
        self.label=QLabel(self)
        self.label.setText("Font")
        self.btn.setGeometry(10,10,100,50)
        self.btn.setText("Выбор шрифта")
        self.btn.clicked.connect(self.color)
        self.show()
    def color(self):
        color_1,ok=QFontDialog.getFont() 
        if ok:
            self.label.setFont(color_1)  
            
            
            
            
a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())             
                                 