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

    def lista(self):
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
                rotated_image = pygame.transform.rotate(image, (cada_bala[2]))
                rotated_image = pygame.transform.scale(rotated_image, (64 * 0.5, 64 * 0.5))
                rotated_image.set_colorkey((39,190,20)) 
                screen.blit(rotated_image, ((cada_bala[0] - rotated_image.get_width() / 2), (cada_bala[1] - (rotated_image.get_height() / 2 )))) 