import socket
import time
from data.players import Players
from data import db_sesion
db_sesion.global_init()
session=db_sesion.create_session()

main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
main_socket.bind(("localhost",10000))
main_socket.setblocking(False)
main_socket.listen(5)

class Local_Player:
    def __init__(self,id,name,sock,addr):
        self.id=id
        self.db:Players=session.get(Players,self.id)
        self.sock=sock
        self.addres=addr
        self.name=name
        self.x=500
        self.y=500
        self.size=50
        self.errors=0
        self.abs_speed=1
        self.x_speed=0
        self.y_speed=0
        
players=[]

while True: 
    try:
        new_socket,addr=main_socket.accept()
        print(f"Подключился {addr}")
        new_socket.setblocking(False)
        players.append(new_socket)
    except BlockingIOError:
        pass 
 
    for sock in players:
        try:
            data=sock.recv(1024).decode()
            print(f"Получил {data}")
        except:
            pass  
    
    for sock in players:
        try:
            sock.send("Cъел".encode())
        except:
            players.remove(sock)
            sock.close()
            print("Пользователь отключен")    
            
            
                             
    time.sleep(1)    