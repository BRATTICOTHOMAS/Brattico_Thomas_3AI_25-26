import pygame

VELOCITA_PESCE = 5
NOME_SCHERMATA_GIOCO = "gioco"
NOME_SCHERMATA_INTRO = "intro"

pygame.init()

sfondo = pygame.image.load('sfondo.jpg')
larghezzaSfondo = sfondo.get_width()
altezzaSfondo = sfondo.get_height()

schermo = pygame.display.set_mode((larghezzaSfondo, altezzaSfondo))
pygame.display.set_caption('Schermo di gioco')
clock = pygame.time.Clock()

pesce = pygame.image.load('pesce.png')
pesce = pygame.transform.scale_by(pesce, 0.5)
larghezzaPesce = pesce.get_width()

schermataIntro = pygame.image.load('schermataIntro.png')
pulsante = pygame.image.load('pulsante.png')
x_pulsante = larghezzaSfondo - pulsante.get_width() - 50
y_pulsante = altezzaSfondo - pulsante.get_height() - 50

schermataCorrente = NOME_SCHERMATA_INTRO

gameOver = False
x = 0
y = 0
xM = 0
yM = 0
while not gameOver:
    
    #eventi
    for event in pygame.event.get():       
        #uscita
        if event.type == pygame.QUIT:
            gameOver = True
        #mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            xM, yM = pygame.mouse.get_pos()

    if schermataCorrente == NOME_SCHERMATA_INTRO:

        #disegno lo sfondo 
        schermo.blit(schermataIntro, (0,0))
        #disegno il pulsante
        schermo.blit(pulsante, (x_pulsante, y_pulsante))

        #se le coordinate del mouse xM e yM collidono con il rettangolo del pulsante passo alla schermata di gioco
        if pulsante.get_rect(topleft=(x_pulsante,y_pulsante)).collidepoint(xM, yM):
            schermataCorrente = NOME_SCHERMATA_GIOCO

    elif schermataCorrente == NOME_SCHERMATA_GIOCO:

        tasti = pygame.key.get_pressed()
        if tasti[pygame.K_w]:
            y -= VELOCITA_PESCE
        if tasti[pygame.K_s]:
            y += VELOCITA_PESCE
        if tasti[pygame.K_a]:
            x -= VELOCITA_PESCE
        if tasti[pygame.K_d]:
            x += VELOCITA_PESCE
        if tasti[pygame.K_q]:
            schermataCorrente = NOME_SCHERMATA_INTRO

        schermo.blit(sfondo, (0,0))
        schermo.blit(pesce, (x,y))
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
           