import pygame
import random
import time

# --- Costanti di Gioco ---
VELOCITA_PESCE = 5
VELOCITA_SQUALO = 3 # Velocità dello squalo che insegue
SCALA_PESCE = 0.5
SCALA_SQUALO = 0.7 
TEMPO_STELLA_VISIBILE = 3000 # La stella resta visibile per 3 secondi (3000 ms)
PUNTI_STELLA = 10
colore_punteggio= (0,0,255)
# --- Configurazione del Timer per la Stella Marina ---
# Usiamo un evento personalizzato per decidere quando la stella deve apparire
EVENTO_STELLA_SPAWN = pygame.USEREVENT + 1 
# La stella apparirà casualmente tra 4 e 8 secondi dopo la scomparsa/raccolta


pygame.init()
pygame.font.init() # Inizializza il modulo dei font per il punteggio

# --- Configurazione dello Schermo e dello Sfondo ---
sfondo = pygame.image.load('sfondo.jpg') # Assicurati di avere 'sfondo.jpg'
larghezzaSfondo = sfondo.get_width()
altezzaSfondo = sfondo.get_height()
schermo = pygame.display.set_mode((larghezzaSfondo, altezzaSfondo))
pygame.display.set_caption('Pesce Contro Squalo (Base)')
clock = pygame.time.Clock()
font_punteggio = pygame.font.Font(None, 36)

# --- 1. Configurazione Pesce (Giocatore) ---
pesce_img_originale = pygame.image.load('pesce.png') # Assicurati di avere 'pesce.png'
pesce = pygame.transform.scale_by(pesce_img_originale, SCALA_PESCE)
larghezzaPesce = pesce.get_width()
altezzaPesce = pesce.get_height()
pesce_sinistra = pygame.transform.flip(pesce, True, False)
pesce_corrente = pesce
x = 0
y = 0
pesce_rect = pesce.get_rect(topleft=(x, y))

# --- 2. Configurazione Squalo (Nemico Inseguitore) ---
squalo_img_originale = pygame.image.load('SQUALO_BIANCO.png') # Assicurati di avere 'squalo.png'
squalo = pygame.transform.scale_by(squalo_img_originale, 0.09)
larghezzaSqualo = squalo.get_width()
squalo_sinistra = pygame.transform.flip(squalo, True, False)
squalo_corrente = squalo


# Posizione iniziale dello squalo (lo facciamo partire dall'angolo in alto a destra)
x_squalo = larghezzaSfondo - larghezzaSqualo
y_squalo = altezzaSfondo 
squalo_rect = squalo.get_rect(topleft=(x_squalo, y_squalo))

# --- 3. Configurazione Stella Marina (Bonus a Tempo) ---
stella_img = pygame.image.load('stella1.png') # Assicurati di avere 'stella.png'
stella = pygame.transform.scale_by(stella_img, 0.2)
stella_visibile = False
stella_tempo_spawn = 0
stella_rect = stella.get_rect(topleft=(-100, -100)) # Inizialmente fuori dallo schermo

# --- Variabili di Stato ---
gameOver = False
punti = 0

# --- Ciclo Principale di Gioco ---
while not gameOver:
    
    # --- Gestione Eventi ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        
        # L'evento timer per lo spawn della stella scatta
        if event.type == EVENTO_STELLA_SPAWN:
            if not stella_visibile: # Appare solo se non è già visibile
                # Posizione casuale
                x_stella = random.randint(0, larghezzaSfondo - stella_rect.width)
                y_stella = random.randint(0, altezzaSfondo - stella_rect.height)
                stella_rect.topleft = (x_stella, y_stella)
                stella_visibile = True
                stella_tempo_spawn = pygame.time.get_ticks() # Registra l'ora di comparsa

    # --- Movimento Pesce (Tastiera + Rotazione + Bordi) ---
    tasti = pygame.key.get_pressed()
    
    if tasti[pygame.K_w]:
        y -= VELOCITA_PESCE
    if tasti[pygame.K_s]:
        y += VELOCITA_PESCE
        
    if tasti[pygame.K_a]:
        x -= VELOCITA_PESCE
        pesce_corrente = pesce_sinistra # Rotazione a sinistra
    if tasti[pygame.K_d]:
        x += VELOCITA_PESCE
        pesce_corrente = pesce         # Rotazione a destra

    # Blocco sui bordi (Horizontal Boundary Check)
    if x < 0:
        x = 0
    elif x > larghezzaSfondo - larghezzaPesce:
        x = larghezzaSfondo - larghezzaPesce

    # Blocco sui bordi (Vertical Boundary Check)
    if y < 0:
        y = 0
    elif y > altezzaSfondo - altezzaPesce:
        y = altezzaSfondo - altezzaPesce
    
    # Aggiorna il rettangolo di collisione del pesce
    pesce_rect.topleft = (x, y)


    # --- Movimento Squalo (Logica di Inseguimento) ---
    # Calcola la direzione verso il pesce e muoviti
    if x_squalo < x:
        x_squalo += VELOCITA_SQUALO
        squalo_corrente = squalo # Gira a destra
    elif x_squalo > x:
        x_squalo -= VELOCITA_SQUALO
        squalo_corrente = squalo_sinistra # Gira a sinistra
        
    if y_squalo < y:
        y_squalo += VELOCITA_SQUALO
    elif y_squalo > y:
        y_squalo -= VELOCITA_SQUALO
        
    # Aggiorna il rettangolo di collisione dello squalo
    squalo_rect.topleft = (x_squalo, y_squalo)
    

    # --- Logica Stella Marina (Timer di 3 secondi) ---
    if stella_visibile:
        tempo_trascorso = pygame.time.get_ticks() - stella_tempo_spawn
        if tempo_trascorso > TEMPO_STELLA_VISIBILE:
            # Tempo scaduto: nascondi la stella e riattiva il timer
            stella_visibile = False
            stella_rect.topleft = (-100, -100) # Sposta fuori dallo schermo
            pygame.time.set_timer(EVENTO_STELLA_SPAWN, random.randrange(4000, 8001))

    
    # --- Collisioni ---
    
    # Collisione 1: Pesce - Squalo
    if pesce_rect.colliderect(squalo_rect):
        print("GAME OVER! Sei stato mangiato dallo Squalo!")
        gameOver = True
        
    # Collisione 2: Pesce - Stella
    if stella_visibile and pesce_rect.colliderect(stella_rect):
        punti += PUNTI_STELLA
        print(f"Stella raccolta! Punti: {punti}")
        stella_visibile = False
        stella_rect.topleft = (-100, -100) # Nascondi immediatamente
        # Riattiva il timer subito per il prossimo spawn
        pygame.time.set_timer(EVENTO_STELLA_SPAWN, random.randrange(4000, 8001))


    # --- Disegno sullo Schermo ---
    schermo.blit(sfondo, (0, 0))
    
    # Disegna gli sprite
    schermo.blit(squalo_corrente, squalo_rect)
    schermo.blit(pesce_corrente, pesce_rect)
    
    if stella_visibile:
        schermo.blit(stella, stella_rect)

    # Disegna il punteggio
    testo_punti = font_punteggio.render(f"Punti: {punti}", True, colore_punteggio)
    schermo.blit(testo_punti, (10, 10))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()