import pygame, sys 
from pygame.locals import * 
from pygame import *
import numpy



class Player():

    def __init__(self, screen,angle, speed,x,y):
        self.y = y
        self.x = x
        self.screen = screen
        self.keys = pygame.key.get_pressed()
        self.angle = angle
        self.speed = speed
        self.timegame = 0


    def draw(self):
        
        image = pygame.image.load("Player.png").convert()
        image = pygame.transform.scale(image, (50, 50))
        image = pygame.transform.rotate(image, self.angle)
        
        if self.x > 832:                                  
            self.x = -32                                  
        if self.x < -32:                                
            self.x = 832                                  
        if self.y > 632:                                  
            self.y = -32                                  
        if self.y < -32:                                
            self.y = 632
        
        if self.keys[pygame.K_LEFT]:
            self.angle += 0.25
        if self.keys[pygame.K_RIGHT]:
            self.angle -= 0.25
        if self.keys[pygame.K_UP]:
            if self.speed > -0.5:                                  
                self.speed -= 0.01
        if self.keys[pygame.K_DOWN]:
            if self.speed < 0:                                   
                self.speed += 0.0005
        if not self.keys[pygame.K_UP]:                           
            if self.speed < 0:                                   
                self.speed += 0.0005
        if self.speed > 0:                                       
            self.speed = 0 

        if self.angle >= 360:
            self.angle = 0
        if self.angle <= -360:
            self.angle = 0

        self.y -= self.speed * numpy.sin(numpy.radians(self.angle * 2))      
        self.x += self.speed * numpy.cos(numpy.radians(self.angle * 2))
        rot_image = pygame.transform.rotate(image, (self.angle + 90))
        rot_image.set_colorkey((39,190,20))  
        
        self.screen.blit(rot_image,(self.x - int(rot_image.get_width() / 2), self.y - int(rot_image.get_height() / 2)))
        
    
        return(self.angle,self.speed, self.x, self.y)