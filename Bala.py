import pygame
import pygame, sys 
from pygame.locals import * 
import numpy
import time

class Balas():
    def __init__(self,x,y,angulo,lista):
        self.lista_de_balas = lista
        minutos = time.gmtime()[4]
        segundos = time.gmtime()[5]
        self.lista_de_balas.append([x , y, (angulo - 90) * 2, 4,minutos,segundos])

    def return_the_list(self):
        return self.lista_de_balas

    def disparo(screen, balas_lista, speed):
        image = pygame.image.load("Bala.png").convert()
        if len(balas_lista) > 0:
            for cada_bala in balas_lista:
                cada_bala[0] += speed * numpy.cos(numpy.radians(cada_bala[2]))
                cada_bala[1] -= speed * numpy.sin(numpy.radians(cada_bala[2]))
                if cada_bala[0] > 816:
                    cada_bala[0] = -16
                if cada_bala[0] < -16:
                    cada_bala[0] = 816
                if cada_bala[1] > 816:
                    cada_bala[1] = -16
                if cada_bala[1] < -16:
                    cada_bala[1] = 816
                rotated_sprite = pygame.transform.rotate(image, (cada_bala[2]))
                rotated_sprite = pygame.transform.scale(rotated_sprite, (64 * 0.5, 64 * 0.5))
                rotated_sprite.set_colorkey((39,190,20)) 
                screen.blit(rotated_sprite, ((cada_bala[0] - rotated_sprite.get_width() / 2), (cada_bala[1] - (rotated_sprite.get_height() / 2 )))) 