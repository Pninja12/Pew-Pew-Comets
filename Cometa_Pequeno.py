import pygame, sys 
from pygame.locals import * 
import numpy

class Cometas_Pequenos():
    def __init__(self,x,y,angulo,lista):
        self.lista_cometa_pequeno = lista
        self.lista_cometa_pequeno.append([x , y, (angulo - 90) * 2, 4])

    def lista(self):
        return self.lista_cometa_pequeno

    def cometa_pequeno_funcao(screen, lista_cometa, speed):
        image = pygame.image.load("Cometa.png").convert()
        if len(lista_cometa) > 0:
            for cada_cometa in lista_cometa:
                cada_cometa[0] += speed * numpy.cos(numpy.radians(cada_cometa[2]))
                cada_cometa[1] -= speed * numpy.sin(numpy.radians(cada_cometa[2]))
                if cada_cometa[0] > 900:
                    cada_cometa[0] = -100
                if cada_cometa[0] < -100:
                    cada_cometa[0] = 900
                if cada_cometa[1] > 900:
                    cada_cometa[1] = -100
                if cada_cometa[1] < -100:
                    cada_cometa[1] = 900
                rotated_image = pygame.transform.rotate(image, (cada_cometa[2]))
                rotated_image = pygame.transform.scale(rotated_image, (50, 50))
                rotated_image.set_colorkey((39,190,20)) 
                screen.blit(rotated_image, ((cada_cometa[0] - rotated_image.get_width() / 2), (cada_cometa[1] - (rotated_image.get_height() / 2 )))) 