import pygame
from pygame.locals import *
pygame.init()
Larghezza= 800
altezza=600
FINESTRA= pygame.display.set_mode((Larghezza,altezza),0,32)
 
piattaforma= pygame.image.load('piattaforma.png')
piattaforma2= pygame.image.load('terra.png')
terra=piattaforma2
terra=pygame.transform.scale(piattaforma2,(Larghezza,98)).convert_alpha()
piattaforma=pygame.transform.scale(piattaforma, (200, 50))
piattaforma2=pygame.transform.scale(piattaforma2,(200,50))
piattaformaX=99
salto=-50
gravità=10
velocità=40
velocità_verticale=0
posizione_terra=altezza-150
basso=posizione_terra
piattaformaY=400
piattaforma2X = 400
piattaforma2Y = 150
direzione="destra"
running = True
jumping=False
framerate=pygame.time.Clock()
pygame.display.set_caption('salta verso il cielo')
sfondo= pygame.image.load('sfondo.jpg').convert_alpha()
personaggio=pygame.image.load('personaggio.png').convert_alpha()
personaggio=pygame.transform.scale(personaggio,(150,150))
rect_personaggio= personaggio.get_rect()
personaggioX=600
personaggioY=350
rect_personaggio= (personaggioX,personaggioY)
pygame.display.update()
running= True
clock=pygame.time.Clock()
move=True
TERRA=True
while running:
    clock.tick(120)
    if direzione=="destra":
        piattaformaX+=10
        piattaforma2X -=11
    if piattaformaX>200 and piattaforma2X<300: direzione="sinistra"
    if direzione=="sinistra":
        piattaformaX-=10
        piattaforma2X +=11
        if piattaformaX<100: direzione="destra"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                personaggioX=personaggioX-velocità
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                personaggioX=personaggioX+(velocità)
                rect_personaggio= (personaggioX,personaggioY)
            if event.key == pygame.K_SPACE or event.key == ord('w'):
                if not jumping:
                     jumping=True
                if jumping:
                    personaggioY= personaggioY+salto
                    rect_personaggio= (personaggioX,personaggioY)
                    personaggioY

                 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                personaggioX=personaggioX-velocità
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                personaggioX=personaggioX+(velocità)
                rect_personaggio= (personaggioX,personaggioY)
            if event.key == ord('q'):
                main = False    
        if basso<posizione_terra:
                basso=posizione_terra
                velocità_verticale=0
                TERRA=True
        if personaggioX<0:
                personaggioX=0
        if personaggioX>Larghezza:
                personaggioX=Larghezza
 
        rect_personaggio= (personaggioX,personaggioY)          
 
    FINESTRA.blit(sfondo, (0, 0))
    FINESTRA.blit(terra,(0,500))
    FINESTRA.blit(personaggio,rect_personaggio)
    FINESTRA.blit(piattaforma, (piattaformaX, piattaformaY))
    FINESTRA.blit(piattaforma2,(piattaforma2X,piattaforma2Y))
    pygame.display.update()
    pygame.display.flip()
 
    framerate.tick(18)