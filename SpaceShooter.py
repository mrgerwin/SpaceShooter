import math
import pygame 
import random
import time
from SpaceShooterSprites import *
import sys

def drawText(font):
    label = font.render("Power: " + str(a_laser.LaserCharge), True, white)
    
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
a_laser = Laser(window, [0,0], 0, 0)

while True:
    FrameNum += 1
    window.fill(black)
    timer.tick(30)
    player.rotate()
    player.move()
    player.draw()
    drawText(font)
    for laser in lasers:
        laser.move()
        laser.rotate()
        laser.draw()
        #Get rid of laser when it hits edge of screen
        if laser.rect.right<=laser.rect.width:
            lasers.remove(laser)
        elif laser.rect.left>screen_size[0]:
            lasers.remove(laser)
        elif laser.rect.top>screen_size[1]:
            lasers.remove(laser)
        elif laser.rect.bottom<=laser.rect.height:
            lasers.remove(laser)
    #pygame.draw.rect(window, white, player.rect)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit = True
            sys.exit(0)
            
        buttonsPressed = pygame.key.get_pressed()
        #print(buttonsPressed)
        if buttonsPressed[pygame.K_SPACE]:
            a_laser.LaserCharge+=1
            print(a_laser.LaserCharge)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                a_laser.LaserCharge = 0
            if event.key == pygame.K_a:
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
            if event.key == pygame.K_SPACE:
                #a_laser = Laser(window, player.rect.topleft, player.angle, 6)
                a_laser.angle = player.angle
                a_laser.rect.x = player.rect.x
                a_laser.rect.y = player.rect.y
                a_laser.speed= 6
                #a_laser.resize()
                lasers.append(a_laser)
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