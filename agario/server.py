import socket
import time
import pygame
import random
import math
from data.players import Players
from data import db_sesion
from russian_names import RussianNames
db_sesion.global_init()
session=db_sesion.create_session()

colors= ['Maroon', 'DarkRed', 'FireBrick', 'Red', 'Salmon',
         'Tomato', 'Coral', 'OrangeRed', 'Chocolate', 'SandyBrown',
         'DarkOrange', 'Orange', 'DarkGoldenrod', 'Goldenrod', 'Gold',
         'Olive', 'Yellow', 'YellowGreen', 'GreenYellow', 'Chartreuse',
         'LawnGreen', 'Green', 'Lime', 'Lime Green', 'SpringGreen', 'MediumSpringGreen',
         'Turquoise', 'LightSeaGreen', 'MediumTurquoise', 'Teal', 'DarkCyan',
         'Aqua', 'Cyan', 'Dark Turquoise', 'DeepSkyBlue', 'DodgerBlue', 
         'RoyalBlue', 'Navy', 'DarkBlue', 'MediumBlue']

pygame.init()
WIDTH_ROOM,HEIGHT_ROOM=4000,4000
WIDTH_SERVER,HEIGHT_SERVER=300,300
FPS=100

MOB_QUANTITY=25
names=RussianNames(count=MOB_QUANTITY*2,patronymic=False,surname=False,rare=True)
names=list(set(names))

FOOD_SIZE=15
FOOD_QUANTITY=int(WIDTH_ROOM*HEIGHT_ROOM/40000)

main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
main_socket.bind(("localhost",10000))
main_socket.setblocking(False)
main_socket.listen(5)


screen=pygame.display.set_mode((WIDTH_SERVER,HEIGHT_SERVER))
pygame.display.set_caption("Agario")
clock=pygame.time.Clock()


class Local_Player:
    def __init__(self,id,name,sock,addr,color):
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
        self.color=color
        self.w_vision=800
        self.h_vision=600
    
    def new_speed(self):
        self.abs_speed=10/math.sqrt(self.size)    
        
    def update(self):
        if self.x-self.size<=0:
            if self.x_speed>=0:
                self.x+=self.x_speed
        elif self.x+self.size>=WIDTH_ROOM:
            if self.x_speed<=0:
                self.x+=self.x_speed
        else:
            self.x+=self.x_speed
        if self.y-self.size<=0:
            if self.y_speed>=0:
                self.y+=self.y_speed
        elif self.y+self.size>=HEIGHT_ROOM:
            if self.y_speed<=0:
                self.y+=self.y_speed                
        else:
             self.y+=self.y_speed 
             
        if self.size>=100:
            self.size-=self.size/18000

    def change_speed(self,vektor):
        vektor=list(map(float,vektor.split(",")))
        if vektor[0]==0 and vektor[1]==0:
            self.x_speed=self.y_speed=0
        else:
            vektor=vektor[0]*self.abs_speed,vektor[1]*self.abs_speed
            self.x_speed=vektor[0]
            self.y_speed=vektor[1] 
             
    def load(self):
        self.size=self.db.size
        self.abs_speed=self.db.abs_speed 
        self.x_speed=self.db.speed_x 
        self.y_speed=self.db.speed_y 
        self.x=self.db.x 
        self.y=self.db.y 
        self.errors=self.db.errors 
        self.color=self.db.color 
        self.h_vision=self.db.h_vision 
        self.w_vision=self.db.w_vision 
        return self
    
    def sync(self):
        self.db.size=self.size
        self.db.abs_speed=self.abs_speed 
        self.db.speed_x=self.x_speed
        self.db.speed_y=self.y_speed
        self.db.x=self.x 
        self.db.y=self.y 
        self.db.errors=self.errors 
        self.db.color=self.color 
        self.db.h_vision=self.h_vision 
        self.db.w_vision=self.w_vision 
        return self                   

class Food:
    def __init__(self,x,y,size,color):
        self.x=x
        self.y=y
        self.size=size
        self.color=color 
        
        
players={}

for x in range(MOB_QUANTITY):
    server_mob = Players(names[x], None)
    server_mob.color = random.choice(colors)
    server_mob.x, server_mob.y = random.randint(0, WIDTH_ROOM),random.randint(0, HEIGHT_ROOM)
    server_mob.speed_x, server_mob.speed_y = random.randint(-1, 1),random.randint(-1, 1)
    server_mob.size = random.randint(10, 100)
    session.add(server_mob)
    session.commit()
    local_mob = Local_Player(server_mob.id, server_mob.name, None, None, "Red").load()
    players[server_mob.id] = local_mob

foods=[]
for i in range(FOOD_QUANTITY):
    foods.append(Food(
        x=random.randint(0,WIDTH_ROOM),
        y=random.randint(0,HEIGHT_ROOM),
        size=FOOD_SIZE,
        color=random.choice(colors)
    ))

run=True
tick=-1
while run:
    clock.tick(FPS)
    tick+=1 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    if tick%200==0:        
        try:
            new_socket,addr=main_socket.accept()
            print(f"Подключился {addr}")
            new_socket.setblocking(False)
            login=new_socket.recv(1024).decode()
            login=login.split(",")
            player=Players(login[1],addr)
            player.color=login[0]
            session.merge(player)
            session.commit()
            addr=f"({addr[0]},{addr[1]})"
            data=session.query(Players).filter(Players.addres==addr).first()
            player=Local_Player(data.id,data.name,new_socket,addr,data.color).load()
            players[data.id]=player
        
        
        except BlockingIOError:
            pass 
        
        need=MOB_QUANTITY-len(players)
        if need>0:
            names=RussianNames(count=need*2,patronymic=False,surname=False,rare=True)
            names=list(set(names))
            for n in range(need):
                server_mob = Players(names[n], None)
                server_mob.color = random.choice(colors)
                spawn:Local_Player=random.choice(foods)
                #foods.remove(spawn)
                server_mob.x, server_mob.y = spawn.x,spawn.y
                server_mob.speed_x, server_mob.speed_y = random.randint(-1, 1),random.randint(-1, 1)
                server_mob.size = random.randint(10, 100)
                session.add(server_mob)
                session.commit()
                local_mob = Local_Player(server_mob.id, server_mob.name, None, None, "Red").load()
                local_mob.new_speed()
                players[server_mob.id] = local_mob
        
        need=FOOD_QUANTITY-len(foods)
        if need>0:
            for n in range(need):
                foods.append(Food(
                x=random.randint(0,WIDTH_ROOM),
                y=random.randint(0,HEIGHT_ROOM),
                size=FOOD_SIZE,
                color=random.choice(colors)
            ))
        
    for id in list(players):
        if players[id].sock is not None:
            try:
                data=players[id].sock.recv(1024).decode()
                #print(f"Получил {data}")
                players[id].change_speed(data)
            except:
                pass  
    
    visibale_bacteries={}
    for id in list(players):
        visibale_bacteries[id]=[]
    pairs=list(players.items())
    for i in range(len(pairs)):
        for j in range(i+1,len(pairs)):
            p_1:Players=pairs[i][1]   
            p_2:Players=pairs[j][1]
            dist_x = p_2.x - p_1.x
            dist_y = p_2.y - p_1.y
            if abs(dist_x) <= p_1.w_vision // 2 + p_2.size and abs(dist_y) <= p_1.h_vision // 2 + p_2.size:
                distance=math.sqrt(dist_x**2+dist_y**2)
                if distance<=p_1.size and p_1.size>p_2.size*1.1:
                    p_1.size=math.sqrt(p_1.size**2+p_2.size**2)
                    p_1.new_speed()
                    p_2.size,p_2.speed_x,p_2.speed_y=0,0,0    
                if p_1.addres is not None:
                    data=f"{round(dist_x)} {round(dist_y)} {round(p_2.size)} {p_2.color}"
                    visibale_bacteries[p_1.id].append(data)
            if abs(dist_x) <= p_2.w_vision // 2 + p_1.size and abs(dist_y) <= p_2.h_vision // 2 + p_1.size:
                distance=math.sqrt(dist_x**2+dist_y**2)
                if distance<=p_2.size and p_2.size>p_1.size*1.1:
                    p_2.size=math.sqrt(p_2.size**2+p_1.size**2)
                    p_2.new_speed()
                    p_1.size,p_1.speed_x,p_1.speed_y=0,0,0 
                if p_2.addres is not None:
                    data=f"{round(-dist_x)} {round(-dist_y)} {round(p_1.size)} {p_1.color}"
                    visibale_bacteries[p_2.id].append(data)  
                    
    for food in foods:
        p_1:Players=pairs[j][1]
        dist_x = food.x - p_1.x
        dist_y = food.y - p_1.y
        if abs(dist_x) <= p_1.w_vision // 2 + food.size and abs(dist_y) <= p_1.h_vision // 2 + food.size:
            distance=math.sqrt(dist_x**2+dist_y**2)
            if distance<p_1.size:
                p_1.size=math.sqrt(p_1.size**2+food.size**2)
                p_1.new_speed()
                food.size=0
                foods.remove(food)   
            if p_1.addres is not None:
                data=f"{round(dist_x)} {round(dist_y)} {round(food.size)} {food.color}"
                visibale_bacteries[p_1.id].append(data)
                        
                      
    #Создаем ответы для каждого игрока.    
    for id in list(players):
        r_=str(round(players[id].size))  
        visibale_bacteries[id]=[r_]+visibale_bacteries[id]  
        visibale_bacteries[id]="$"+",".join(visibale_bacteries[id])
                    

    #Отправляем информацию игрокам.
    for id in list(players):
        if players[id].sock is not None:
            try:
                players[id].sock.send(visibale_bacteries[id].encode())
            except:
                players[id].sock.close()
                del players[id]
                session.query(Players).filter(Players.id==id).delete()
                session.commit()
                print("Пользователь отключен")
        else:
            if tick%400==0:
                players[id].change_speed(f"{random.randint(-1,1)},{random.randint(-1,1)}")
    
    for id in list(players):
        if players[id].errors>=500 or players[id].size==0:
            if players[id].sock is not None:
               players[id].sock.close()   
            del players[id]
            session.query(Players).filter(Players.id==id).delete()
            session.commit()
                
    #Рисуем окно сервера               
    screen.fill('black') 
    for id in players:
        player = players[id]
        x = player.x * WIDTH_SERVER // WIDTH_ROOM
        y = player.y * HEIGHT_SERVER // HEIGHT_ROOM
        size = player.size * WIDTH_SERVER // WIDTH_ROOM
        pygame.draw.circle(screen, player.color, (x, y), size)
        
    for id in players:
        player = players[id]
        players[id].update()
    
    pygame.display.update()           
            
pygame.quit()           
main_socket.close()
session.query(Players).delete()
session.commit()                             
        