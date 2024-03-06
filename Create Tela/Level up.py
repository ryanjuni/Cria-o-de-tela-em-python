import pygame
from pygame.locals import *
from sys import exit

pygame.init()

BRANCO = (255,255,255)
LARGURA = 720
ALTURA = 500

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Level up')
relogio = pygame.time.Clock()


while True:
    relogio.tick(30)
    tela.fill (BRANCO)  # Preenche a tela

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()            