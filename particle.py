import pygame
from random import *
import colorsys
from math import *

# pygame setup
pygame.init()
width,height = 1000,800
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
wid,hei = width/2,height/2
clock = pygame.time.Clock()
running = True
particles = []   
# mousex , mousey =0, 0
# def mousemove():
mousex , mousey = pygame.mouse.get_pos()
    # for i in range(100):
    #     particles.append(particle())
    
t=pygame.Color(20,20,20)
# pygame.Color.a = 1
# t.premul_alpha()
# hue = 0  # Hue value between 0 and 1
# saturation = 1  # Saturation value between 0 and 1
# lightness = 0.5  # Lightness value between 0 and 1
# r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
# color = (r*255,g*255,b*255)
          
class particle():
    def __init__(self):
        self.size = uniform(10,20)
        self.x = mousex#randrange(self.size,width-self.size)
        self.y = mousey#randrange(self.size,height-self.size)
        self.hue = 0  # Hue value between 0 and 1
        self.saturation = 1  # Saturation value between 0 and 1
        self.lightness = 0.5  # Lightness value between 0 and 1
        # self.r, self.g, self.b = colorsys.hls_to_rgb(self.hue, self.lightness, self.saturation)
         # Increment hue (and wrap around at 1)
    
    # Convert HSL to RGB
        self.r, self.g, self.b = colorsys.hls_to_rgb(self.hue, self.lightness, self.saturation)
        self.color = (int(self.r * 255), int(self.g * 255), int(self.b * 255)) 
        # self.color =(self.r*255,self.g*255,self.b*255)
        # self.color = color
        self.sx = randint(-3,3)
        self.sy = randint(-3,3)
        
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.size)
    def update(self):
        self.draw()
        
        # self.x = mousex
        # self.y = mousey
        # self.lightness+=10
        self.hue = (self.hue + 0.005) % 1
        self.r, self.g, self.b = colorsys.hls_to_rgb(self.hue, self.lightness, self.saturation)
        self.color = (int(self.r * 255), int(self.g * 255), int(self.b * 255)) 
        self.x += self.sx
        self.y += self.sy
        if self.size>0.2:
            self.size-=0.08
        
def init():
    # Get the relative mouse movement
    rel = pygame.mouse.get_rel()

    # Check if the mouse is moving
    if rel != (0, 0):
        
        for i in range(3):
            # x = mousex
            # y = mousey
            # sx = uniform(-3,3)
            # sy = uniform(-3,3)
            obj  = particle()
            particles.append(obj)
            
            # print(obj.x)
        
def particlehandler():
    
    for obj in particles:
        # obj.x = mousex
        # obj.y = mousey
        # obj.draw()
        obj.update()
        for o in particles:
            dx = obj.x - o.x
            dy = obj.y - o.y
            distance = sqrt(dx*dx+dy*dy)
            if distance<100:
                pygame.draw.line(screen,obj.color,(obj.x,obj.y),(o.x,o.y),int(obj.size/10))
                
        if obj.size <0.3:
            particles.remove(obj)      
            # print(len(particles))
        
# init()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mousex , mousey = pygame.mouse.get_pos()
            particlehandler()
            init()
            
            
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(t)

    # RENDER YOUR GAME HERE
    # pygame.draw.circle(screen,"white",(wid,hei),20)
    # wid+=1
    # mousex , mousey = pygame.mouse.get_pos()
    
    init()
    particlehandler()
    
    # a=  particle(mousex,mousey,0,0)
    # a.update()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # clock.tick(100)  # limits FPS to 60

pygame.quit()