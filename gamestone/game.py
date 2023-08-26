from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction
import sys
from PyQt5.QtGui import QPixmap,QIcon
import random
from PyQt5.QtCore import Qt



class Game(QMainWindow):
    def __init__(self,count_stone):
        super().__init__()
        uic.loadUi("gamestone\\game.ui",self)
        self.count_stone=count_stone
        self.btn_group.buttonClicked.connect(self.buttons)
        self.toolbar=QToolBar(self)
        self.toolbar.setObjectName("toolbar")
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea,self.toolbar)
        self.plus=QAction(QIcon("gamestone/Restart.png"),"+",self)
        self.toolbar.addAction(self.plus)
        self.plus.triggered.connect(self.start)
        self.update()                        
    def update(self,player_take="",com_take=""):
        self.count_stone_lbl.setText(f"Кол-во камней:{self.count_stone}")
        self.player_take_lbl.setText(f"Вы взяли:{player_take}")
        self.bot_take_lbl.setText(f"Взял компьютер: {com_take}")
        if self.count_stone<=0:
            for n in self.btn_group.buttons():
                n.setEnabled(False)         
    def buttons(self,btn):
        self.count_stone-=int(btn.text())
        if self.count_stone<=0:
            self.label_2.setText("Вы победили!Игра окончена!")
            self.update(btn.text(),0)
        else:  
            com_take=self.count_stone%4
            if com_take==0:
                com_take=random.randint(1,3)
            self.count_stone-=com_take
            if self.count_stone<=0:
                self.label_2.setText("Вы проиграли!Игра окончена!")   
            self.update(btn.text(),com_take)
    def start(self):
        self.count_stone=random.randint(15,30)
        self.update()
        for n in self.btn_group.buttons():
            n.setEnabled(True) 
    def keyPressEvent(self,e):
        if e.key()==Qt.Key_R:
            self.start()             
                           
 

            
                
        
        