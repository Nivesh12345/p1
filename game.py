import os
import pygame
import pyautogui
from math import *
from Particle import *
from random import *

# pygame setup
pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
wid, hei = width/2, height/2
clock = pygame.time.Clock()
running = True

a, b = wid+100, hei     
radius = 100
angle = 0 
pos_x = 0  
pos_y = 0

speed = 5  
space_pressed = False
mousepressed = False

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
    # Set window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
    os.environ['SDL_VIDEO_CENTERED'] = '0'
    screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen
    screen.fill("black")

    # Get global mouse position using pyautogui
    global_mouse_pos = pyautogui.position()
    
    # Calculate mouse position relative to Pygame window
    x = global_mouse_pos.x - pos_x
    y = global_mouse_pos.y - pos_y

    # Draw center circle
    pygame.draw.circle(screen,"white",(wid,hei),30,5)
    
    # Calculate angle to mouse
    dx = x - wid
    dy = y - hei
    angle = atan2(dy,dx)
    
    # Calculate point on circular path
    a = (radius * cos(angle)) + wid
    b = (radius * sin(angle)) + hei
    
    # Draw line from center to circular path point
    pygame.draw.line(screen,"white",(wid,hei),(a,b))
    
    # Keyboard controls
    keys = pygame.key.get_pressed()
    
    # Shooting controls
    if keys[pygame.K_SPACE] and not space_pressed:
        balls.append(ball(wid,hei,5,angle))
        space_pressed = True 
    elif not keys[pygame.K_SPACE]:
        space_pressed = False
    
    # Mouse controls
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0] and not mousepressed:
        balls.append(ball(wid,hei,5,angle))
        mousepressed = True     
    elif not mouse_buttons[0]:
        mousepressed = False
    
    # Movement controls
    if keys[pygame.K_d]:
        wid += speed
    if keys[pygame.K_a]:
        wid -= speed
    if keys[pygame.K_w]:
        hei -= speed
    if keys[pygame.K_s]:
        hei += speed
    
    # Ball management
    for obj in balls:
        if obj.b.position.getx() > obj.radius + width or obj.b.position.getx() < -obj.radius:
            balls.remove(obj)
            width += 30
            pos_x += 30
        if obj.b.position.gety() > obj.radius + height or obj.b.position.gety() < -obj.radius:
            balls.remove(obj)
            height += 30
            pos_y += 30  
        obj.check()
    
    # Enemy management
    for e in enemys:
        e.check()   
    
    # Gradual window shrinking
    else:
        height -= 0.6      
        pos_y -= 0.6    
        width -= 0.6    
        pos_x += 0.6    
    
    # Print global and local mouse positions for debugging
    print(f"Global Mouse Position: {global_mouse_pos}")
    print(f"Local Mouse Position: ({x}, {y})")
    
    # Update display
    pygame.display.flip()
    clock.tick(100)  # limits FPS to 100

pygame.quit()