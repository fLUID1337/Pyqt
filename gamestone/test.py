from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction
import sys
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.toolbar=QToolBar(self)
        self.toolbar.setObjectName("toolbar")
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea,self.toolbar)
        self.toolbar.addAction(self.plus)
        self.show()
    def start(self):
        print("ббаб")     
            
    
    
    
    
a = QApplication(sys.argv)
d = Main()
sys.exit(a.exec())     