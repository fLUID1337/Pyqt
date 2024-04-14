import pygame

FPS=65
WIDTH=800
HEIGHT=600
KIRPICH_WIDTH_COUNT=10
KIRPICH_HEIGHT_COUNT=5
KIRPICH_HEIGHT=20
KIRPICH_WIDTH=WIDTH/KIRPICH_WIDTH_COUNT


WHITE=(255,255,255)
YELLOW=(255,255,0)
BROWN=(140,112,76)

pygame.init()

#класс платформы
class Platform:
    def  __init__(self):
        self.x=300
        self.y=500
        self.speed=0
        self.height=20
        self.width=200
        
    def update(self):
        self.x+=self.speed
        pygame.draw.rect(screen,(0,200,0),(self.x,self.y,self.width,self.height))
        
        #отскоки платформы
        if self.x<=0:
            self.speed=-self.speed
            
        if self.x+200>=WIDTH:
            self.speed=-self.speed
              
#класс кирпича        
class Kirpich:
    def __init__(self,x,y):
        self.x=x        
        self.y=y
    
    def update(self):
        pygame.draw.rect(screen,BROWN,(self.x,self.y, KIRPICH_WIDTH, KIRPICH_HEIGHT))          
        pygame.draw.rect(screen,(0,0,0),(self.x,self.y, KIRPICH_WIDTH, KIRPICH_HEIGHT),1)          
        
#класс мяча        
class Ball:
    def __init__(self,x,y,radius=10):
        self.x=x       
        self.y=y
        self.speed_x=-1
        self.speed_y=-5
        self.radius=radius
        self.score=0
        self.run=True
    
    def update(self):
        self.x+=self.speed_x
        self.y+=self.speed_y
        pygame.draw.circle(screen, YELLOW, (self.x,self.y), self.radius) 
        pygame.draw.circle(screen, (0,0,0), (self.x,self.y), self.radius,1) 
        
        #отскоки мяча
        if self.y-self.radius<=0:
            self.speed_y=-self.speed_y
            
        if self.y+self.radius>=HEIGHT:
            self.run=False
            
        if self.x-self.radius<=0:
            self.speed_x=-self.speed_x
            
        if self.x+self.radius>=WIDTH:
            self.speed_x=-self.speed_x 
    
    def hit(self,all_kirpich:list[Kirpich]):
        for kirpich in all_kirpich:
            if self.y-self.radius<kirpich.y+KIRPICH_HEIGHT:
                if self.x+self.radius>kirpich.x and self.x-self.radius<kirpich.x+KIRPICH_WIDTH:
                    self.speed_y=-self.speed_y
                    all_kirpich.remove(kirpich)
                    self.score+=1 
                    
            if self.y+self.radius>kirpich.y and self.y+self.radius<kirpich.y+KIRPICH_HEIGHT:
                if self.x+self.radius>kirpich.x and self.x-self.radius<kirpich.x+KIRPICH_WIDTH:
                    self.speed_y=-self.speed_y
                    all_kirpich.remove(kirpich) 
                    self.score+=1 
                     
            if self.x-self.radius>kirpich.x and self.x-self.radius<kirpich.x+KIRPICH_HEIGHT:
                if self.y>kirpich.y and self.y<kirpich.y+KIRPICH_HEIGHT:
                    self.speed_x=-self.speed_x
                    all_kirpich.remove(kirpich) 
                    self.score+=1  
            
            if self.x+self.radius>kirpich.x and self.x+self.radius<kirpich.x+KIRPICH_HEIGHT:
                if self.y>kirpich.y and self.y<kirpich.y+KIRPICH_HEIGHT:
                    self.speed_x=-self.speed_x
                    all_kirpich.remove(kirpich)
                    self.score+=1    
                    
    def hit_platform(self,pl:Platform):
        if self.y+self.radius>pl.y and self.y+self.radius<pl.y+pl.height:
            if self.x+self.radius>pl.x and self.x-self.radius<pl.x+pl.width:
                self.speed_y=-self.speed_y                                             
            

def message(text):
    t=font.render(text,True,(0,0,0))
    screen.blit(t,(WIDTH-80,HEIGHT-30))
    

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Кирпичики")
clock=pygame.time.Clock()

font=pygame.font.Font(None,26)

platform=Platform()
ball=Ball(400,480)

all_kirpich=[]

x=0
y=0

for i in range(KIRPICH_HEIGHT_COUNT):
    for j in range(KIRPICH_WIDTH_COUNT):
        all_kirpich.append(Kirpich(x,y))
        x+=KIRPICH_WIDTH
    y+=KIRPICH_HEIGHT
    x=0
    

tick=-1


while ball.run:
    clock.tick(FPS)
    tick+=1 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                platform.speed=-5 
            if event.key==pygame.K_RIGHT:
                platform.speed=5        
    screen.fill(WHITE)
    platform.update()
    for kirpich in all_kirpich:
        kirpich.update()
    ball.hit(all_kirpich)
    ball.hit_platform(platform)
    ball.update()
    message(f"Счет:{ball.score}")
    pygame.display.flip()
pygame.quit()            
