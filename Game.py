import pygame, sys
from pygame.locals import * 
import numpy
import time
import random
#import dos ficheiros
from Jogador import Player
from Bala import Balas
from Cometa_Grande import Cometas_Grandes
from Cometa_Medio import Cometas_Medios
from Cometa_Pequeno import Cometas_Pequenos

pygame.init()

#chamas as variáveis

myfont = pygame.font.Font('arial.ttf',35)
fontname = pygame.font.Font('arial.ttf',40)
exit = myfont.render('EXIT' , True , (255,255,255))
start = myfont.render('START' , True , (255,255,255))
name = fontname.render('Pew-Pew-Comets' , True , (255,255,255))
life = fontname.render('LIFE:' , True , (255,255,255))
gameover = fontname.render('Game Over' , True , (255,255,255))
highscore_text = fontname.render('HIGHSCORE' , True , (255,255,255))
highscore_text1 = myfont.render('HIGHSCORE' , True , (255,255,255))
ask = myfont.render('Write 3 letters and then hit Enter' , True , (255,255,255))
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
quantos_cometas = 0
dificuldade_cometas = 1
dificuldade_balas = 1
time_dificuldade = 0
time_dificuldade2 = 0
mudança = 0
one_time = 0
cometas_grandes_lista = []
cometas_medios_lista = []
cometas_pequenos_lista = []
destruido = 0
player_life = 0
life_lost = 0
perder_vida = 0
perder_vida2 = 0
score = 0
highscore_data = []
name_highscore = ""
best_score = []
ativar_leaderboard = 0


keys=pygame.key.get_pressed()
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("COMETS") 

player_image = pygame.image.load("Player.png").convert()
player_image = pygame.transform.scale(player_image, (40, 40))
player_image.set_colorkey((39,190,20)) 

#começa o programa
while True:
    screen.fill((0,10,20))
    current_time.append(time.gmtime()[4])  
    current_time.append(time.gmtime()[5])
    current_time.append(time.gmtime()[3])
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
        if keys[K_ESCAPE]:
            pygame.quit() 
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN and (300 <= rato[0] <= 400 and 250 <= rato[1] <= 300):  #evento para os botões do menu inicial
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and (300 <= rato[0] <= 400 and 150 <= rato[1] <= 200):  #evento para os botões do menu inicial
            comeco = 1
        if event.type == pygame.MOUSEBUTTONDOWN and (300 <= rato[0] <= 400 and 200 <= rato[1] <= 250): 
            comeco = 4
    if keys[K_SPACE]:  #evento de tiros
        if tiro_recente2 != current_time[0]:
            tiro_recente2 = current_time[0]
            tiro_recente = -1
        if tiro_recente < current_time[1]:
            if dificuldade_balas == 3:
                balas_lista = Balas(jogador.x, jogador.y, jogador.angle, balas_lista).lista()
                balas_lista = Balas(jogador.x, jogador.y, jogador.angle, balas_lista).lista()
                balas_lista = Balas(jogador.x, jogador.y, jogador.angle, balas_lista).lista()
            elif dificuldade_balas == 2:
                balas_lista = Balas(jogador.x, jogador.y, jogador.angle, balas_lista).lista()
                balas_lista = Balas(jogador.x, jogador.y, jogador.angle, balas_lista).lista()
            else:
                balas_lista = Balas(jogador.x, jogador.y, jogador.angle, balas_lista).lista()
            quantas_balas += 1
            tiro_recente = current_time[1]
    rato = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    jogador = Player(screen, angle, speed, playerx,playery)
    
    #começo o menu
    if comeco == 0:
        while(True):
            if 300 <= rato[0] <= 400 and 150 <= rato[1] <= 200:
                pygame.draw.rect(screen,(255,0,0),[300,150,210,40])


            elif 300 <= rato[0] <= 400 and 200 <= rato[1] <= 250:
                pygame.draw.rect(screen,(255,0,0),[300,200,210,40])

            elif 300 <= rato[0] <= 400 and 250 <= rato[1] <= 300:
                pygame.draw.rect(screen,(255,0,0),[300,250,210,40])

            screen.blit(start , (300,150))
            screen.blit(exit , (300,250))
            screen.blit(highscore_text1, (300,200))
            screen.blit(name , (200,50))
            break
    #começa o jogo
    if comeco == 1:
        screen.blit(life , (0,0))
        if player_life >= 3:
            screen.blit(player_image, (180,0))

        if player_life >= 2:
            screen.blit(player_image, (140,0))

        if player_life >= 1:
            screen.blit(player_image, (100,0))

        if one_time == 0:
            time_dificuldade2 = time.gmtime()[3]
            time_dificuldade = time.gmtime()[4]
            perder_vida = time.gmtime()[5]
            perder_vida1 = time.gmtime()[4]
            player_life = 3
            one_time = 1
            highscore = 0
            playerx = 0
            playery = 0
        
        
        if dificuldade_cometas <= 3:
            if time_dificuldade2 != current_time[2]:
                time_dificuldade -= 60
                mudança = 1
            if current_time[0] - time_dificuldade == 3:
                dificuldade_balas += 1
                dificuldade_cometas += 1
                if mudança == 1:
                    time_dificuldade += 60
                    mudança = 0
                time_dificuldade2 = time.gmtime()[3]
                time_dificuldade = time.gmtime()[4]
            
        Balas.disparo(screen,balas_lista, 1)
        
        all = jogador.draw()
        angle = all[0]
        speed = all[1]
        playerx = all[2]
        playery = all[3]
        
        if quantas_balas > 0:
                for todas in balas_lista:
                    if todas[4] != current_time[0]:
                        current_time[1] += 60
                    if int(current_time[1]) - int(todas[5]) >= 3:
                        balas_lista.pop(0)
        if quantos_cometas < dificuldade_cometas:
            cometas_grandes_lista = Cometas_Grandes(random.randint(0,800), 0, random.randint(0,359), cometas_grandes_lista).lista()
            quantos_cometas += 1

            
        cont_balas = 0
        for todas_balas in balas_lista:
            bala_col = pygame.Rect(todas_balas[0], todas_balas[1], 64 * 0.5, 64 * 0.5)
            
            cont_com = 0
            for lista_dos_cometas_grandes in cometas_grandes_lista:
                cometa_col = pygame.Rect(lista_dos_cometas_grandes[0], lista_dos_cometas_grandes[1], 200, 200)
                collide = cometa_col.colliderect(bala_col)

                if collide == True:
                    balas_lista.pop(cont_balas)
                    score += 10
                    cometas_medios_lista = Cometas_Medios(lista_dos_cometas_grandes[0], lista_dos_cometas_grandes[1], random.randint(0,359), cometas_medios_lista).lista()
                    cometas_medios_lista = Cometas_Medios(lista_dos_cometas_grandes[0], lista_dos_cometas_grandes[1], random.randint(0,359), cometas_medios_lista).lista()
                    cometas_medios_lista = Cometas_Medios(lista_dos_cometas_grandes[0], lista_dos_cometas_grandes[1], random.randint(0,359), cometas_medios_lista).lista()

                    cometas_grandes_lista.pop(cont_com)
                    quantos_cometas -= 1
                    destruido = 1
                    break
                cont_com += 1


            if destruido == 1:
                destruido = 0
                break

            cont_com = 0
            for lista_dos_cometas_medios in cometas_medios_lista:
                cometa_col = pygame.Rect(lista_dos_cometas_medios[0], lista_dos_cometas_medios[1], 100, 100)
                collide = cometa_col.colliderect(bala_col)

                if collide == True:
                    balas_lista.pop(cont_balas)
                    score += 15
                    cometas_pequenos_lista = Cometas_Pequenos(lista_dos_cometas_medios[0], lista_dos_cometas_medios[1], random.randint(0,359), cometas_pequenos_lista).lista()
                    cometas_pequenos_lista = Cometas_Pequenos(lista_dos_cometas_medios[0], lista_dos_cometas_medios[1], random.randint(0,359), cometas_pequenos_lista).lista()
                    cometas_pequenos_lista = Cometas_Pequenos(lista_dos_cometas_medios[0], lista_dos_cometas_medios[1], random.randint(0,359), cometas_pequenos_lista).lista()
                    cometas_pequenos_lista = Cometas_Pequenos(lista_dos_cometas_medios[0], lista_dos_cometas_medios[1], random.randint(0,359), cometas_pequenos_lista).lista()
                    cometas_pequenos_lista = Cometas_Pequenos(lista_dos_cometas_medios[0], lista_dos_cometas_medios[1], random.randint(0,359), cometas_pequenos_lista).lista()

                    cometas_medios_lista.pop(cont_com)
                    destruido = 1
                    break
                cont_com += 1

            if destruido == 1:
                destruido = 0
                break

            cont_com = 0
            for lista_dos_cometas_pequenos in cometas_pequenos_lista:
                cometa_col = pygame.Rect(lista_dos_cometas_pequenos[0], lista_dos_cometas_pequenos[1], 50, 50)
                collide = cometa_col.colliderect(bala_col)

                if collide == True:
                    balas_lista.pop(cont_balas)
                    score += 20
                    cometas_pequenos_lista.pop(cont_com)
                    destruido = 1
                    break
                cont_com += 1
            cont_balas += 1

            if destruido == 1:
                destruido = 0
                break

        if perder_vida1 != current_time[0]:
            perder_vida1 = current_time[0]
            perder_vida = -1
        if perder_vida < current_time[1]: 
            cont_com = 0
            for lista_dos_cometas_grandes in cometas_grandes_lista:
                cometa_col = pygame.Rect(lista_dos_cometas_grandes[0], lista_dos_cometas_grandes[1], 160, 160)
                player_col = pygame.Rect(playerx, playery, 50, 50)
                collide = cometa_col.colliderect(player_col)

                if collide == True:
                    player_life -= 1
                    life_lost = 1
                    cometas_grandes_lista.pop(cont_com)
                    quantos_cometas -= 1
                    destruido = 1
                    break
                cont_com += 1

            if life_lost == 1:
                playerx = 400
                playery = 300
                life_lost = 0

            cont_com = 0
            for lista_dos_cometas_medios in cometas_medios_lista:
                cometa_col = pygame.Rect(lista_dos_cometas_medios[0], lista_dos_cometas_medios[1], 60, 60)
                player_col = pygame.Rect(playerx, playery, 50, 50)
                collide = cometa_col.colliderect(player_col)

                if collide == True:
                    player_life -= 1
                    life_lost = 1
                    cometas_medios_lista.pop(cont_com)
                    destruido = 1
                    break
                cont_com += 1

            if life_lost == 1:
                playerx = 400
                playery = 300
                life_lost = 0

            cont_com = 0
            for lista_dos_cometas_pequenos in cometas_pequenos_lista:
                cometa_col = pygame.Rect(lista_dos_cometas_pequenos[0], lista_dos_cometas_pequenos[1], 10, 10)
                player_col = pygame.Rect(playerx, playery, 50, 50)
                collide = cometa_col.colliderect(player_col)
                
                if collide == True:
                    player_life -= 1
                    life_lost = 1
                    cometas_pequenos_lista.pop(cont_com)
                    destruido = 1
                    break
                cont_com += 1
            cont_balas += 1

            if life_lost == 1:
                playerx = 400
                playery = 300
                life_lost = 0
            
        if player_life <= 0:
            comeco = 3


        Cometas_Grandes.cometa_grande_funcao(screen,cometas_grandes_lista, 0.5)
        Cometas_Medios.cometa_medio_funcao(screen,cometas_medios_lista, 0.5)
        Cometas_Pequenos.cometa_pequeno_funcao(screen,cometas_pequenos_lista, 0.5)
    
    if comeco == 3:
        screen.fill((0,10,20))
        screen.blit(gameover , (290,50))
        screen.blit(ask , (150,100))

        time.sleep(3)
        pygame.display.update()
        pygame.display.flip()
        name_highscore = input("Write here: ")

        
        highscore_data = [score," ",name_highscore]
        with open("highscore.txt", "a") as file:
            for variable in highscore_data:
                file.write(str(variable))
            file.write("\n")
        file.close()
        ativar_leaderboard = 1
        comeco = 0
        time.sleep(5) 
    if comeco == 4:
        with open("highscore.txt", "r") as file:
            for line in file:

                # reading each word 
                numbers_highscore = 0
                letter_highscore = ""
                after_number = 0       
                for word in line.split():
                    if after_number == 0:
                        numbers_highscore = word
                        after_number = 1
                    else:
                        letter_highscore = word
                best_score.append([int(numbers_highscore),letter_highscore])
        file.close()

        best_score.sort(reverse=True) 
        pygame.display.update()
        pygame.display.flip()
        best_score1 = myfont.render(str(best_score[0]) , True , (255,255,255))
        best_score2 = myfont.render(str(best_score[1]) , True , (255,255,255))
        best_score3 = myfont.render(str(best_score[2]) , True , (255,255,255))
        screen.fill((0,10,20))
        screen.blit(highscore_text , (300,0))
        screen.blit(best_score1 , (350,100))
        screen.blit(best_score2 , (350,150))
        screen.blit(best_score3 , (350,200))
        comeco = 0
        pygame.display.update()
        pygame.display.flip()
        time.sleep(5) 
        for delete in best_score:
            best_score.pop(0)
    


    
    pygame.display.update()
    pygame.display.flip()

    current_time.pop(0)
    current_time.pop(0)
    current_time.pop(0)

#referencias

#https://www.pygame.org/docs/ref/event.html#module-pygame.event
#https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
#https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
#https://stackoverflow.com/questions/23142712/pygame-images-move-with-rotation
#https://stackoverflow.com/questions/57226587/image-rotation-while-moving
#Colega Diogo Caetano a22204491