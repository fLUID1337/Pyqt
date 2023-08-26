from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QPixmap


class num1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("menu\\menu.ui", self)
        photo_1 = QPixmap("menu\\img\\блюдо1.jpg")
        photo_1 = photo_1.scaled(100, 70)
        self.img_1.setPixmap(photo_1)
        photo_2 = QPixmap("menu\\img\\блюдо2.jpg")
        photo_2 = photo_2.scaled(100, 70)
        self.img_2.setPixmap(photo_2)
        photo_3 = QPixmap("menu\\img\\блюдо3.jpg")
        photo_3 = photo_3.scaled(100, 70)
        self.img_3.setPixmap(photo_3)
        self.spin_1.valueChanged.connect(self.spin)
        self.spin_2.valueChanged.connect(self.spin)
        self.spin_3.valueChanged.connect(self.spin)
        self.btn.clicked.connect(self.chek)
        self.summa=0
        self.chek_w=chek()
        self.chek_w.btn.clicked.connect(self.chek_w.close)
        self.show()

    def spin(self):
        self.summa = self.spin_1.value()*250+self.spin_2.value()*150+self.spin_3.value()*100
        self.summa_l.setText(str(self.summa)+"р.")

    def chek(self):
        chek_text=f'''Жаркое x{self.spin_1.value()} \t {self.spin_1.value()*250}р.
Салат x{self.spin_2.value()} \t {self.spin_2.value()*150}р.
Напиток x{self.spin_3.value()} \t {self.spin_3.value()*100}р.
Сумма \t\t {self.summa}р.'''
        self.chek_w.setChek(chek_text)
        self.chek_w.show()
class chek(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("menu\\chek.ui", self)
        #self.btn.clicked.connect(self.close)
    def setChek(self,text):
        self.label.setText(text) 
         
                
a = QApplication(sys.argv)
d = num1()
sys.exit(a.exec())
