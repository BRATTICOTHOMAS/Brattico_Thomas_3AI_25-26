import pygame
import random
import time
 
pygame.init()
schermo=pygame.display.set_mode((800,400))
pygame.display.set_caption("GOBLIN")
clock=pygame.time.Clock()
 
gameOver = False
#tempo
 
 
 
sfondo=pygame.image.load("sfondo.jpg")
goblin=pygame.image.load("Screenshot 2025-12-09 100817.png")
goblin=pygame.transform.scale(goblin,(0.5,0.5))
bomba=pygame.image.load("bomb-2025548_1280.webp")
#ANIMAZIONE
esplosione= [
    pygame.image.load('explosion-153710_1280.webp'),
    pygame.image.load('explosion_f.png'),
    pygame.image.load('QDRW6hHQtWE-CjPf.webp')
]
tipo_espl=0
conta=0
tempo1=pygame.time.get_ticks()
tempo=0
pygame.mouse.set_visible(False)
pos_bomba=(400,200)
while not gameOver:
    tasti=pygame.key.get_pressed()
    mouse=pygame.mouse.get_pos()
    pos_HK=(mouse[0]-3,mouse[1]-150)
    #eventi
    for event in pygame.event.get():      
        #uscita
        if event.type == pygame.QUIT:
            gameOver = True
           
        if event.type==pygame.MOUSEBUTTONUP:
           
            pos_bomba=(mouse[0]-100,mouse[1]+50)
           
        if tasti[pygame.K_ESCAPE]:
            gameOver=True
   
       
           
    schermo.blit(sfondo,(0,0))
    schermo.blit(goblin,(mouse))
    schermo.blit(bomba,(pos_bomba))
    #ANIMAZIONE
    if event.type==pygame.MOUSEBUTTONUP:        
        if tempo>1000:
            conta+=1
            if conta>=20:
                tipo_espl+=1
                conta=0
                if tipo_espl>=3:
                    tipo_espl=0
            schermo.blit(esplosione[tipo_espl],(pos_bomba))
    pygame.display.update()
    clock.tick(60)
    tempo2=pygame.time.get_ticks()#misura il tempo
    tempo=tempo2-tempo1
pygame.quit