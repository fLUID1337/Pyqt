from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton, QSplitter,QHBoxLayout,QSlider,QCalendarWidget
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt,QDate

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.calendar=QCalendarWidget(self)
        self.lbl=QLabel(self)
        self.lbl.setGeometry(100,200,150,100)
        self.calendar.clicked[QDate].connect(self.showDate)
        self.show()
    def showDate(self,date:QDate):
        self.lbl.setText(date.toString())
            
        





a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())                 
