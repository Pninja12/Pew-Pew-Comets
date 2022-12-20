import pygame, sys 
from pygame.locals import * 


pygame.init()

myfont = pygame.font.Font('arial.ttf',35)
fontname = pygame.font.Font('arial.ttf',40)
exit = myfont.render('EXIT' , True , (255,255,255))
start = myfont.render('START' , True , (255,255,255))
name = fontname.render('Pew-Pew-Comets' , True , (255,255,255))
comeco = 0
red = [200,50,50]
white = [255,255,255]
playerx = 100
playery = 100

screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("COMETS") 

def player(x,y):
    pygame.draw.line(screen,red, (x - 25,y + 25), (x,y - 25),2)
    pygame.draw.line(screen,red, (x,y - 25), (x + 25,y + 25),2)
    pygame.draw.line(screen,white, (x + 25,y + 25), (x - 25,y + 25),2)

keys=pygame.key.get_pressed()
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit() 
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN and (300 <= rato[0] <= 400 and 200 <= rato[1] <= 250):
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and (300 <= rato[0] <= 400 and 150 <= rato[1] <= 200):
            comeco = 1
    
    rato = pygame.mouse.get_pos()
    if comeco == 0:
        while(True):
            pygame.draw.rect(screen,(0,0,0),[300,150,100,40])
            pygame.draw.rect(screen,(0,0,0),[300,200,100,40])
            if 300 <= rato[0] <= 400 and 150 <= rato[1] <= 200:
                pygame.draw.rect(screen,(255,0,0),[300,150,150,40])


            elif 300 <= rato[0] <= 400 and 200 <= rato[1] <= 250:
                pygame.draw.rect(screen,(255,0,0),[300,200,150,40])

            screen.blit(start , (300,150))
            screen.blit(exit , (300,200))
            screen.blit(name , (200,100))
            break
    else:
        player(playerx, playery)
    pygame.display.update()



#referencias

#https://www.pygame.org/docs/ref/event.html#module-pygame.event
#https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
#https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/