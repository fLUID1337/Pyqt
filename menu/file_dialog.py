from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton,QFileDialog
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt





class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.btn=QPushButton(self)
        self.btn.setGeometry(10,10,100,50)
        self.btn.setText("Выбор цвета")
        self.btn.clicked.connect(self.color)
        self.show()
    def color(self):
        color_1=QFileDialog.getOpenFileName(self,"Выберите файл","/home","Картинки (*.png, *.jpg)") 
        print(color_1) 
            
            
            
            
a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())             
                                 