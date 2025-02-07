import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("El juego de la banana 🍌🍊")

# Colores
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 0, 0)

# Cargar imágenes
banana_img = pygame.image.load("banana.png")
banana_img = pygame.transform.scale(banana_img, (80, 80))
orange_img = pygame.image.load("orange.png")
orange_img = pygame.transform.scale(orange_img, (100, 100))

# Cargar sonidos
frotar_sound = pygame.mixer.Sound("frotar.wav")  # Sonido cuando se mueve
chorro_sound = pygame.mixer.Sound("chorro.wav")  # Sonido del "evento especial"

# Posiciones iniciales
banana_x = WIDTH // 2 - 40
banana_y = HEIGHT // 2
orange1_x = WIDTH // 4 - 50
orange2_x = WIDTH * 3 // 4 - 50
orange_y = HEIGHT // 2

# Variables del juego
speed = 10
clicks = 0
chorreando = False
chorro_intensity = 0  # Nivel de "presión"

# Bucle principal
running = True
while running:
    screen.fill(WHITE)

    # Dibujar naranjas
    screen.blit(orange_img, (orange1_x, orange_y))
    screen.blit(orange_img, (orange2_x, orange_y))

    # Dibujar banana
    screen.blit(banana_img, (banana_x, banana_y))

    # Dibujar barra de intensidad
    pygame.draw.rect(screen, RED, (50, 350, chorro_intensity * 5, 20))

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
            chorro_intensity += 1
            banana_x += random.choice([-speed, speed])  # Movimiento interactivo
            frotar_sound.play()  # Reproducir sonido de fricción

            # Si se alcanzan muchos clics, activar "chorreo"
            if clicks > 10:
                chorreando = True
                chorro_sound.play()  # Reproducir sonido del "evento"

    # Efecto de "chorreo"
    if chorreando:
        for i in range(chorro_intensity):
            pygame.draw.circle(screen, BLUE, (banana_x + 40, banana_y + 70 + i * 5), 5)  # Gotas cayendo

    pygame.display.update()

pygame.quit()