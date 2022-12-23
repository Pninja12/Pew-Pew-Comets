import pygame, sys
from pygame.locals import * 
import numpy
import time
#import dos ficheiros
from Jogador import Player
from Bala import Balas

pygame.init()

#chamas as variáveis
myfont = pygame.font.Font('arial.ttf',35)
fontname = pygame.font.Font('arial.ttf',40)
exit = myfont.render('EXIT' , True , (255,255,255))
start = myfont.render('START' , True , (255,255,255))
name = fontname.render('Pew-Pew-Comets' , True , (255,255,255))
comeco = 0
red = [150,100,100] 
white = [255,255,255]
angle = 0
speed = 0
playerx = 400
playery = 300
balas_lista = []
current_time = []
tiro_recente = 0
tiro_recente2 = 0
quantas_balas = 0


keys=pygame.key.get_pressed()
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("COMETS") 

#começa o programa
while True:
    screen.fill((0,10,20))
    current_time.append(time.gmtime()[4])  
    current_time.append(time.gmtime()[5])
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
        if keys[K_ESCAPE]:
            pygame.quit() 
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN and (300 <= rato[0] <= 400 and 200 <= rato[1] <= 250):  #evento para os botões do menu inicial
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and (300 <= rato[0] <= 400 and 150 <= rato[1] <= 200):  #evento para os botões do menu inicial
            comeco = 1
    if keys[K_SPACE]:  #evento de tiros
        if tiro_recente2 != current_time[0]:
            tiro_recente2 = current_time[0]
            tiro_recente = 0
        if tiro_recente < current_time[1]:
            balas_lista = Balas(jogador.x, jogador.y, jogador.angle, balas_lista).return_the_list()
            quantas_balas += 1
            tiro_recente = current_time[1]
    rato = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    jogador = Player(screen, angle, speed, playerx,playery)
    
    #começo o menu
    if comeco == 0:
        while(True):
            if 300 <= rato[0] <= 400 and 150 <= rato[1] <= 200:
                pygame.draw.rect(screen,(255,0,0),[300,150,150,40])


            elif 300 <= rato[0] <= 400 and 200 <= rato[1] <= 250:
                pygame.draw.rect(screen,(255,0,0),[300,200,150,40])

            screen.blit(start , (300,150))
            screen.blit(exit , (300,200))
            screen.blit(name , (200,50))
            break
    #começa o jogo
    else:
        Balas.disparo(screen,balas_lista, 1)
        all = jogador.draw()
        angle = all[0]
        speed = all[1]
        playerx = all[2]
        playery = all[3]
        if quantas_balas > 0:
            for i in range(quantas_balas):
                for todas in balas_lista:
                    if todas[4] != current_time[0]:
                        current_time[1] += 60
                    if int(current_time[1]) - int(todas[5]) >= 3:
                        balas_lista.pop(0)
    pygame.display.update()
    pygame.display.flip()

    current_time.pop(0)
    current_time.pop(0)

#referencias

#https://www.pygame.org/docs/ref/event.html#module-pygame.event
#https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
#https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
#https://stackoverflow.com/questions/23142712/pygame-images-move-with-rotation
#https://stackoverflow.com/questions/57226587/image-rotation-while-moving
#Colega Diogo Caetano a22204491
