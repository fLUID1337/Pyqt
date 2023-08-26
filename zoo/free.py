from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton,QFileDialog,QFontDialog,QHBoxLayout,QVBoxLayout,QComboBox
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.label=QLabel(self)
        combo=QComboBox(self)
        combo.addItem("Математика")
        combo.addItem("Русский язык")
        combo.addItem("Столовая")
        combo.addItem("физкультура")
        combo.addItem("Музыка")
        combo.activated[str].connect(self.onActivated)
        self.show()
    def onActivated(self,text):
        self.label.setText(text)    






a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())        