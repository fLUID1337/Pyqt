from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QPixmap
import sqlite3

class PasswordError(Exception):
    pass

class LenghtError(PasswordError):
    pass
    
class DigitError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class SequenceError(PasswordError):
    pass

class CopyError(PasswordError):
    pass

con=sqlite3.connect("authentication//users.db")
cursor=con.cursor()

integer=[0,1,2,3,4,5,6,7,8,9]
integer=set(map(str,integer))
alfavit=['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю',
        'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
low=set("".join(alfavit))
up=set("".join(alfavit).upper())
spec=set(["!","#","?","$","%","&"])

class Registration(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("authentication\\registration.ui", self)
        self.btn.clicked.connect(self.registration)
    def registration(self):
        username_my=self.user_edit.text()
        password=self.password_edit.text()    
        password_re=self.password_re_edit.text()
        #print(username_my,password,password_re)
        user=cursor.execute(f"select username from users where username='{username_my}'").fetchone()
        if user:
            print("Такой пользователь занят")
        elif len(password)<=7:
            print("Пароль слишком короткий.")
        try:    
            if not(integer & set(password)):raise DigitError("В пароле нет числа.")
            if not(low & set(password)):raise LetterError("В пароле нет маленьких английских букв.")
            if not(up & set(password)):raise LetterError("В пароле нет больших английских букв.")
            if not(spec & set(password)):raise LetterError("В пароле нет спец символов.")
            if not(password_re == password):raise CopyError("Пароли не совпадают.")
        except PasswordError as e:
            self.lbl.setText(str(e))                   
        else:
            cursor.execute(f"insert into users (username,password) values ('{username_my}','{password}')")
            cursor.execute('commit')
            self.close()



      
               
        
       