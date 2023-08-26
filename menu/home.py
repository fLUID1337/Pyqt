from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton,QFileDialog,QFontDialog
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.label=QLabel(self)
        self.label.setGeometry(10,10,300,200)
        self.btn=QPushButton(self)
        self.btn.clicked.connect(self.color)
        self.btn.setGeometry(100,250,100,50)
        self.btn.setText("Выбор шрифта")
        self.btn2=QPushButton(self)
        self.btn2.clicked.connect(self.file)
        self.btn2.setGeometry(250,250,100,50)
        self.btn2.setText("Выбор Файла")
        self.show()
    def color(self):
        color_1,ok=QFontDialog.getFont() 
        if ok:
            self.label.setFont(color_1)
    def file(self):
        color_1=QFileDialog.getOpenFileName(self,"Выберите файл","/home","Файлы (*.txt)")
        print(color_1) 
        with open(color_1[0],"rt",encoding="utf8") as file:
            self.label.setText(file.read())      
            
            
a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())            