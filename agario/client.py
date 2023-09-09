import socket
import time
import pygame

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
sock.connect(("localhost",10000))

pygame.init()
width=800
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Agario")
run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    sock.send("Привет".encode())
pygame.quit()    
    