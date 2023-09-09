import socket
import time

main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
main_socket.bind(("localhost",10000))
main_socket.setblocking(False)
main_socket.listen(5)

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
    time.sleep(1)    