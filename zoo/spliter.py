from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton, QSplitter,QHBoxLayout
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.label=QLabel(self)
        self.lbl=QLabel(self)
        self.setGeometry(10,10,600,600)
        self.label.setPixmap(QPixmap("zoo\\img\\dog.png").scaledToWidth(200))
        self.lbl.setPixmap(QPixmap("zoo\\img\\fox.png").scaledToWidth(200))
        layout=QHBoxLayout(self)
        splitter=QSplitter(Qt.Horizontal)
        splitter.addWidget(self.label)
        splitter.addWidget(self.lbl)
        layout.addWidget(splitter)
        self.setLayout(layout)
        self.show()
        




a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())          