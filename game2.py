import os
import pygame
import pyautogui
from math import *
from Particle import *
from random import *

# pygame setup
pygame.init()
width,height = 800,800
screen = pygame.display.set_mode((width, height))
# screen1 = pygame.display.set_mode((width, height))d 
wid,hei = width/2,height/2
clock = pygame.time.Clock()
running = True

a,b = wid+100,hei     
radius = 100
angle = 0 
pos_x = 0  
pos_y = 0

speed  = 5  
class ball():
    def __init__(self,x,y,speed,angle) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.color = "white"
        self.b = particle(self.x,self.y,self.speed,self.angle)
        self.radius = 10
        self.acc = vector(1,1)
        
        
    def check(self):
        pygame.draw.circle(screen,self.color,(self.b.position.getx(),self.b.position.gety()),self.radius)
        self.b.update()
        # self.b.acclerate(self.acc)
        
class enemy():
    def __init__(self,x,y,speed,angle) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.color = "red"
        self.b = particle(self.x,self.y,self.speed,self.angle)
        self.radius = 20
        self.acc = vector(1,1)
        # self.ball = ball 
        # self.dx = self.b.position.getx() - self.ball.position.getx()
        # self.dy = self.b.position.gety() - self.ball.position.gety()
        # self.distance = sqrt(pow(self.dx,2)+pow(self.dy,2))
        
        
    def check(self):
        pygame.draw.circle(screen,self.color,(self.b.position.getx(),self.b.position.gety()),self.radius,5)
        if self.b.position.getx() >=width+self.radius:
            self.b.position.setx(-self.radius) 
        if self.b.position.getx() < -self.radius:
            self.b.position.setx(width+self.radius) 
        if self.b.position.gety() >=height+self.radius:
            self.b.position.sety(-self.radius) 
        if self.b.position.gety() < -self.radius:
            self.b.position.sety(height+self.radius)
        # if self.distance <= self.radius+self.ball.radius:
             
            
        
        self.b.update()
        
        

balls = []
enemys = []
for i in range(10):
    enemy_x = randint(0,width)
    enemy_y = randint(0,height)
    enemy_speed = randint(-2,2)
    enemy_angle = uniform(-2*pi,2*pi)
    enemys.append(enemy(enemy_x,enemy_y,enemy_speed,enemy_angle,))
    
    
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
    os.environ['SDL_VIDEO_CENTERED'] = '0'
    screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # screen1.fill("black")
    # m_x, m_y = pygame.mouse.get_pos()
    # x = wid 
    # y = hei
    # screen.fill("black")
    # pos_x+=100
    p = pyautogui.position()
    # print(pos_x)
    pygame.draw.circle(screen,"white",(wid,hei),30,5)
    pygame.draw.circle(screen,"white",(wid,hei),30,5)
    
    # dx = (pos_x+wid) - m_x
    # dy = (pos_y+hei) - m_y
    # distance = sqrt(dx*dx + dy*dy)
    # angle = atan2(dy,dx)
    # print(angle)
    x,y = pygame.mouse.get_pos()
    
    # angle -=1 *pi/180   
    a = (radius*  cos(angle)) + wid
    b= (radius* sin(angle)) + hei
    dx = x-wid
    dy = y-hei
    angle = atan2(dy,dx)
    # pygame.draw.circle(screen,color,(int(ball.position.getx()),int(ball.position.gety())),20)
    pygame.draw.line(screen,"white",(wid,hei),(a,b))
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
        # color = "white"
        # ball.velocity.setangle(angle)
        # ball.velocity.setlength(5)
    if keys[pygame.K_SPACE] and not space_pressed:
        balls.append(ball(wid,hei,5,angle))
        # print("Space key pressed")
        
        space_pressed = True 
    elif not keys[pygame.K_SPACE]:
        # Reset the flag when the key is released
        space_pressed = False
    mouse_buttons = pygame.mouse.get_pressed()

    # Check if the left mouse button is pressed
    if mouse_buttons[0] and not mousepressed:
        balls.append(ball(wid,hei,5,angle))
        mousepressed = True     
    elif not mouse_buttons[0]:
        
        mousepressed = False
        # print("Left mouse button pressed")
    if keys[pygame.K_d]:
        wid+=speed
        
    if keys[pygame.K_a]:
        wid-=speed
    if keys[pygame.K_w]:
        hei-=speed
    if keys[pygame.K_s]:
        hei+=speed
    
    for obj in balls:
        if obj.b.position.getx() > obj.radius + width or obj.b.position.getx() < -obj.radius :
                balls.remove(obj)
                width+=30
                pos_x +=30
        if obj.b.position.gety() > obj.radius + height or obj.b.position.gety() < -obj.radius :
                balls.remove(obj)
                height+=30
                pos_y +=30  
        obj.check()
        print(len(balls))   
    for e in enemys:
        e.check()   
    
    
                
        # dx = ball.b.position.getx() - enemy.b.position.getx()
        # dy = ball.b.position.gety() - enemy.b.position.gety()
        # distance = sqrt(pow(dx,2)+ pow(dy,2))
        # if distance <= enemy.radius + ball.radius:
        #     enemys.remove(enemy)
                
                
                

    # RENDER YOUR GAME HERE 
    # width+=10
    # pos_x +=10
    else:
        height-=0.6      
        pos_y -=0.6    
        width-=0.6    
        pos_x +=0.6    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(100)  # limits FPS to 60

pygame.quit()