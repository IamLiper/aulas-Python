import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

largura = 640
altura = 480
x_snake = int(largura/2)
y_snake = int(altura/2)

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game 0.1')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_a]:
            x_snake = x_snake - 20
        if pygame.key.get_pressed()[K_d]:
            x_snake = x_snake + 20
        if pygame.key.get_pressed()[K_w]:
            y_snake = y_snake - 20
        if pygame.key.get_pressed()[K_s]:
            y_snake = y_snake + 20
        
    snake = pygame.draw.rect(tela, (0,255,0), (x_snake,y_snake,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))

    if snake.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1

    tela.blit(texto_formatado, (450,40))
    pygame.display.update()