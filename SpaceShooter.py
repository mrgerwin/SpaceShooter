import math
import pygame 
import random
import time
from SpaceShooterSprites import *
import sys


def maskCollide(ship, points):
    biggest = 0
    smallest = 99999999999
    for pt in points:
        if pt[0] > biggest:
            biggest = pt[0]
        if pt[0] < smallest:
            smallest = pt[0]
    width = biggest-smallest
    biggest = 0
    smallest = 99999999999
    for pt in points:
        if pt[1] > biggest:
            biggest = pt[1]
        if pt[1] < smallest:
            smallest = pt[1]
    height = biggest-smallest
    newSurface = pygame.Surface((width, height), pygame.SRCALPHA)
    theRect = pygame.draw.polygon(newSurface, red, points)
    newMask = pygame.mask.from_surface(newSurface)
    #newMaskImg = newMask.to_surface()
    #window.blit(newMaskImg, theRect)
    X = ship.rect.x-theRect.x
    Y = ship.rect.y-theRect.y
    drawText(font, str(X) + ", "+ str(Y))
    if ship.mask.overlap(newMask, (ship.rect.x-theRect.x, ship.rect.y-theRect.y)):
        return True
    else:
        return False

def LineCollide(ship, pt1, pt2):
    clipped_line = ship.rect.clipline(pt1, pt2)
    
    if len(clipped_line) > 0:
        return True
    else:
        return False

def drawPolyLine():
    rect1 = pygame.draw.line(window, red, points[0], points[1])
    rect2 = pygame.draw.line(window, red, points[1], points[2])
    rect3 = pygame.draw.line(window, red, points[2], points[0])
    
    return [rect1, rect2, rect3]
def drawText(font, text):
    label = font.render(text, True, white)
    
    window.blit(label, (130, 20))
    
black = [0 ,0,0]
white = [255, 255, 255]
red = [255, 0, 0]
screen_size = [800,800]
window = pygame.display.set_mode(screen_size)
timer = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("consolas", 30)
FrameNum = 0
player = Ship(window, [400, 400])
points = [(100, 100), (150, 150), (200, 100), (100, 100)]
#linestriangle = pygame.draw.lines(window, red, False, points)
#triangle = pygame.draw.polygon(window, red, points)

#theMask = pygame.mask.from_surface(triSurface)
#theMaskImage = theMask.to_surface()

lasers = []

while True:
    FrameNum += 1
    window.fill(black)
    timer.tick(30)
    player.rotate()
    player.move()
    player.draw()
    rects = drawPolyLine()
    print(maskCollide(player, points))
    #pygame.draw.rect(window, white, linestriangle)
    #pygame.draw.polygon(window, red, points)
    #linestriangle = pygame.draw.lines(window, red, False, points)
    #window.blit(theMaskImage,[0,0])
    for laser in lasers:
        laser.move()
        laser.draw()
    #pygame.draw.rect(window, white, player.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit = True
            #pygame.quit()
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