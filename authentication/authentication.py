from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QPixmap
from registration import Registration
from login import Login


class num1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("authentication\\main.ui", self)
        self.reg_w=Registration()
        self.registr.clicked.connect(self.reg_w.show)
        self.log_w=Login()
        self.enter.clicked.connect(self.log_w.show)
        self.show()
        
        
        
        
a = QApplication(sys.argv)
d = num1()
sys.exit(a.exec())        