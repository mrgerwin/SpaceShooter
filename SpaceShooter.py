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

def slope(pt1, pt2):
    
    num = pt2[1]-pt1[1]
    den = pt2[0]-pt1[0]
    
    if den==0:
        answer = 0
    else:
        answer = num/den
    return answer

def hitRect(pt1, pt2):
    pointsOnLine = []
    hitRects = []
    deltax = int(abs(pt2[0]-pt1[0]))
    for i in range(deltax):
        pointOnLine = [pt1[0]+i, pt1[1]+i*slope(pt1, pt2)]
        pointsOnLine.append(pointOnLine)
    
    for pt in pointsOnLine:
        a_hitRect = pygame.Rect(pt[0], pt[1], 1, 1)
        hitRects.append(a_hitRect)
    
    return hitRects

def drawPolyLine():
    rect1 = pygame.draw.line(window, red, points[0], points[1])
    rect2 = pygame.draw.line(window, red, points[1], points[2])
    rect3 = pygame.draw.line(window, red, points[2], points[0])
    
    hitRects1 = hitRect(points[0], points[1])
    hitRects2 = hitRect(points[1], points[2])
    hitRects3 = hitRect(points[0], points[2])
    
    allhitRects = []
    allhitRects=hitRects1.copy()
    allhitRects=hitRects2.copy()
    allhitRects=hitRects3.copy()
    
    for rec in hitRects1:
        pygame.draw.rect(window, yellow, rec)
    for rec in hitRects2:
        pygame.draw.rect(window, blue, rec)
        #print(rec)
    for rec in hitRects3:
        pygame.draw.rect(window, green, rec)
    
    #print(allhitRects)
    
    return allhitRects
def drawText(font, text):
    label = font.render(text, True, white)
    
    window.blit(label, (130, 20))
    
black = [0 ,0,0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [10, 10, 100]
yellow = [255, 255, 0]
green = [0, 100, 10]
screen_size = [800,800]
window = pygame.display.set_mode(screen_size)
timer = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("consolas", 30)
FrameNum = 0
player = Ship(window, [400, 400])
points = [(100, 100), (150, 150), (200, 100)]
#linestriangle = pygame.draw.lines(window, red, False, points)
#triangle = pygame.draw.polygon(window, red, points)

#theMask = pygame.mask.from_surface(triSurface)
#theMaskImage = theMask.to_surface()

lasers = []
#rects = drawPolyLine()
while True:
    FrameNum += 1
    window.fill(black)
    timer.tick(30)
    player.rotate()
    player.move()
    player.draw()
    rects = drawPolyLine()
    
    for rect in rects:
        if player.rect.colliderect(rect):
            print("Collision")
    
    """NOT NEEDED IF USING RECT COLLIDE
    #Create rects Masks
    rectsMasks = []
    for rect in rects:
        rect_mask = pygame.mask.Mask((rect.width, rect.height), fill = True)
        rectsMasks.append(rect_mask)
    """
    """FIX OFFSET CODE
    for i in range(len(rectsMasks)):
        offset = (player.rect.x-rects[i].x, player.rect.y-rects[i].y)
        if player.mask.overlap(rectsMasks[i], offset):
            print("collision")
    """
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