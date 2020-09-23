import pygame
import math
from queue import PriorityQueue
from globals import *
from utils import *

WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path Finding")

LINHAS = 50

largura = WIDTH #int(input("Entre com a largura"))

grid = make_grid(LINHAS, largura)

inicio = None
fim = None

run = True
started = False
while (run):
    draw(WIN,grid, LINHAS, WIDTH)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
        if( started ):
            continue
        if (pygame.mouse.get_pressed()[0]): # botão esquerdo do mouse
            pos = pygame.mouse.get_pos()
            linha, coluna = get_click_pos(pos, LINHAS, largura)
            quad = grid[linha][coluna]

            if ( not inicio):
                inicio = quad
                inicio.set_inicio()
            elif (not fim and inicio != quad):
                fim = quad
                fim.set_fim()
            elif( quad != inicio and quad != fim ):
                quad.set_barreira()
        elif (pygame.mouse.get_pressed()[2]): # botão direito do mouse
            pass

pygame.quit()