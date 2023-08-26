from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QPixmap
import sqlite3

class LoginError(Exception):
    pass


class PasswordError(LoginError):
    pass

class NotFoundError(LoginError):
    pass
con=sqlite3.connect("authentication//users.db")
cursor=con.cursor()

class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("authentication\\login.ui", self)
        self.btn.clicked.connect(self.login)
    def login(self):
        username_my=self.user_edit.text()
        password_my=self.password_edit.text()
        try:
            user=cursor.execute(f"select username from users where username='{username_my}'").fetchone() 
            if not(user): raise NotFoundError("Такого пользователя не существует.")
            password=cursor.execute(f"select password from users where username='{username_my}'").fetchone() [0]
            print(password,password_my)
            if not(password==password_my):raise PasswordError("Пароль не верный.")
        except LoginError as e:
            self.lbl.setText(str(e))
        else:
            class num1(QWidget):    
                def __init__(self):
                    super().__init__()
                    
                   
           
            
            