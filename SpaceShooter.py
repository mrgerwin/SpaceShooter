import math
import pygame 
import random
import time
from SpaceShooterSprites import *

def drawText(font):
    label = font.render("Default", True, white)
    
    window.blit(label, (130, 20))
    
black = [0 ,0,0]
white = [255, 255, 255]
screen_size = [800,800]
window = pygame.display.set_mode(screen_size)
timer = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("consolas", 30)
FrameNum = 0
player = Ship(window, [400, 400])
lasers = []

while True:
    FrameNum += 1
    window.fill(black)
    timer.tick(30)
    player.rotate()
    player.move()
    player.draw()
    for laser in lasers:
        laser.move()
        laser.draw()
    #pygame.draw.rect(window, white, player.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit = True
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                a_laser = Laser(window, player.rect.topleft, player.angle, 6)
                lasers.append(a_laser) 
            elif event.key == pygame.K_a:
                player.TurnSpeed=player.TurnAcceleration
                #print(player.TurnSpeed)
            if event.key == pygame.K_d:
                player.TurnSpeed=-player.TurnAcceleration
                #print(player.TurnSpeed)
            if event.key == pygame.K_w:
                player.accelerate()
            if event.key == pygame.K_LEFT:
                player.TurnSpeed=player.TurnAcceleration
                #print(player.TurnSpeed)
            if event.key == pygame.K_RIGHT:
                player.TurnSpeed=-player.TurnAcceleration
                #print(player.TurnSpeed)
            if event.key == pygame.K_UP:
                player.accelerate()
            if event.key == pygame.K_DOWN:
                player.slow()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_LEFT:
                player.TurnSpeed=0
            if event.key == pygame.K_RIGHT:
                player.TurnSpeed=0  
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_a:
                player.TurnSpeed=0
            if event.key == pygame.K_d:
                player.TurnSpeed=0
    pygame.display.update()