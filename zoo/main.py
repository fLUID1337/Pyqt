from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton,QFileDialog,QFontDialog,QHBoxLayout,QVBoxLayout
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        files=["cat.jpg","dog.png","fox.png","ktoto.jpg","panda.jpg","puma.jpeg"]
        titles=["Кот","Собка","Лиса","Ктото","Панда","Пума"]
        layout=QHBoxLayout()
        for k in range(len(files)):
            self.label=QLabel(self)
            inner=QVBoxLayout()
            label_img=QLabel(self)
            label_img.setPixmap(QPixmap("zoo\\img\\"+files[k]).scaledToWidth(200))
            inner.addWidget(label_img)
            label_text=QLabel(titles[k])
            inner.addWidget(label_text)
            layout.addLayout(inner)
        self.setLayout(layout)
        self.show()    
            


a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())          