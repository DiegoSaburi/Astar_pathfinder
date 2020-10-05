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
                print(f"Inicio nas coordenadas X={coluna} Y={linha}")
            elif (not fim and inicio != quad):
                fim = quad
                fim.set_fim()
                print(f"Fim nas coordenadas X={coluna} Y={linha}")
            elif( quad != inicio and quad != fim ):
                quad.set_barreira()
        elif (pygame.mouse.get_pressed()[2]): # botão direito do mouse
            pos = pygame.mouse.get_pos()
            linha, coluna = get_click_pos(pos, LINHAS, largura)
            quad = grid[linha][coluna]
            quad.reset()
            if(quad == inicio):
                inicio = None
            if(quad == fim):
                fim = None
            
        if ( event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE and not started):
                for row in grid:
                    for quad in row:
                        quad.update_vizinhos(grid)
                algorithm(lambda: draw(WIN, grid, LINHAS, WIDTH), grid, inicio, fim )


pygame.quit()