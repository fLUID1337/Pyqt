from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton,QInputDialog
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt





class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        self.label=QLabel(self)
        self.label.move(40,40)
        self.btn=QPushButton(self)
        self.btn.clicked.connect(self.eat)
        self.btn.setGeometry(250,510,150,30)
        self.btn.setText("Заказать")
        self.setGeometry(350,350,550,600)
        photo_1 = QPixmap("menu\\img\\блюдо1.jpg")
        photo_1 = photo_1.scaled(500, 500)
        self.label.setPixmap(photo_1)
        self.show()
    def eat(self):
        text,ok=QInputDialog.getText(self,"?","Вы хотите есть?")
        text1,ok=QInputDialog.getText(self,"?","Вы в этом уверены?")
        text2,ok=QInputDialog.getText(self,"?","А может вам показалось?")
        text3,ok=QInputDialog.getText(self,"?","Так вы хотите заказать еду?")
        text4,ok=QInputDialog.getText(self,"?","А у вас есть деньги?")
        text5,ok=QInputDialog.getText(self,"?","Поделитесь?")
        text6,ok=QInputDialog.getText(self,"?","так вы готовы сделать заказ?")
        text7,ok=QInputDialog.getText(self,"?","Может передумаете?")
        info=text+" "+text1+" "+text2+" "+text3+" "+text4+" "+text5+" "+text6+" "+text7
        self.label.setText(info)
        
        
        
        
        
        
        
        
        
        
            



a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())             
                    