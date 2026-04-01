import math
import pygame 
import random
import time

Speeds = [[0,1],[0,2],[0,3],[1,1], [1,2], [1,3], [-1, 1], [-1, 2], [-1, 3], [2, 1], [2, 2], [2, 3], [-2, 1], [-2, 2], [-2, 3], [0,-1],[0,-2],[0,-3],[1,-1], [1,-2], [1,-3], [-1, -1], [-1, -2], [-1, -3], [2, -1], [2, -2], [2, -3], [-2, -1], [-2, -2], [-2, -3]]

class Ship:
    def __init__(self, window, position):
        self.window = window
        self.OriginalImage = pygame.image.load("Frigate3.png")
        self.image = self.OriginalImage
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.angle = 0
        self.speed = [0,0]
        self.acceleration = 4
        self.TurnSpeed = 0
        self.TurnAcceleration = 4
        self.imageGo = pygame.image.load("Frigate3Go.png")
    
    def accelerate(self):
        self.speed[0] += (self.acceleration/4)*math.cos((self.angle*math.pi)/180)
        self.speed[1] -= (self.acceleration/4)*math.sin((self.angle*math.pi)/180)
    
    def slow(self):
        self.speed[0] -= (self.acceleration/6)*math.cos((self.angle*math.pi)/180)
        self.speed[1] += (self.acceleration/6)*math.sin((self.angle*math.pi)/180)
    
    def rotate(self):
        tempSurface = pygame.Surface([800, 800])
        self.angle += self.TurnSpeed
        originalPosition = self.rect.topleft
        originalCenter = self.rect.center
        self.image = pygame.transform.rotate(self.OriginalImage, self.angle)
        newRect = self.image.get_rect()
        self.rect.topleft = [originalCenter[0]-int(newRect.width/2), originalCenter[1]-int(newRect.height/2)]
        self.rect = tempSurface.blit(self.image, self.rect)
    
    def move(self):
        self.rect.x += self.speed[0]  
        self.rect.y += self.speed[1]
    
    def draw(self):
        #pygame.draw.rect(self.window, [255, 255,255], self.rect)
        self.rect = self.window.blit(self.image, self.rect)

class Laser:
    def __init__(self, screen, position, angle, speed):
        self.Originalimg = pygame.image.load("LaserBeam.png")
        self.angle = angle
        self.window = screen
        self.image = self.Originalimg
        self.speed = speed
        #self.Laserimage = pygame.transform.rotate(self.Laserimage, self.angle)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.newRect = ""
        self.originalCenter = ""
        self.originalPosition = ""
        self.rotate()
        
    def rotate(self):
        self.originalPosition = self.rect.topleft
        self.originalCenter = self.rect.center
        self.image = pygame.transform.rotate(self.Originalimg, self.angle)
        self.newRect = self.image.get_rect()
    
    def move(self):
        self.rect.x+= self.speed*math.cos((self.angle*math.pi)/180)
        self.rect.y-= self.speed*math.sin((self.angle*math.pi)/180)
    
    def draw(self):
        self.rect = self.window.blit(self.image, self.rect)