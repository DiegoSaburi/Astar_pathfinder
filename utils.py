from objects import *
from globals import *
import pygame
def h(p1 : tuple,p2 : tuple):
    '''
    Retorna a distancia entre os pontos p1 e p2
    retorna: float
    '''
    x1,y1 = p1
    x2,y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)
def make_grid (linhas : int,largura : int):
    '''
    Montará o grid
    retorna lista de listas
    '''
    grid = []
    gap = largura // linhas #tamanho da largura de cada cubo do grid
    for i in range(linhas):
        grid.append([])
        for j in range(linhas):
            quad = Quadrado(i,j, gap, linhas)
            grid[i].append(quad) #cada quadrado criado será adicionado na linha

    return grid

def draw_grid (window, linha : int, largura : int):
    '''
    Desenhará as linhas do grid
    '''
    gap = largura//linha
    for i in range(linha):
        pygame.draw.line(window, GREY, (0 , i * gap) , (largura , i*gap)) #desenha as linhas horizontais
        for j in range(linha):
            pygame.draw.line(window, GREY, ( j* gap , 0 ), (j*gap , largura)) #desenha as linhas verticais

def draw(window, grid : list, linha : int, largura : int):

    window.fill(WHITE) #irá pintar toda a window de branco

    for row in grid:
        for quad in row:
            quad.desenhar(window) #irá desenhar os quadrados da grid
    
    draw_grid(window, linha, largura)
    pygame.display.update()

def get_click_pos(pos, linha, largura):
    gap = largura // linha
    y,x = pos

    linha = y // gap
    coluna = x//gap

    return linha,coluna

def algorithm(draw, grid : list, inicio : Quadrado, fim : Quadrado):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, inicio))

    came_from = {}
    g_score = {quad : float("inf") for row in grid for quad in row}
    g_score[inicio] = 0
    f_score = {quad : float("inf") for row in grid for quad in row}
    f_score[inicio] = h(inicio.get_pos(), fim.get_pos())

    open_set_hash = {inicio}

    while ( not open_set.empty() ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        atual = open_set.get()[2]
        open_set_hash.remove(atual)

        if atual == fim:
            return True
        
        for vizinho in atual.vizinhos:
            aux_g_score = g_score[atual] + 1

            if aux_g_score < g_score[vizinho]:
                came_from[vizinho] = atual
                g_score[vizinho] = aux_g_score
                f_score[vizinho] = aux_g_score + h(vizinho.get_pos(), fim.get_pos())
                if vizinho not in open_set_hash:
                    count += 1
                    open_set.put((f_score[vizinho],count, vizinho))
                    open_set_hash.add(vizinho)
                    vizinho.set_aberto()
        
        draw()

        if atual != inicio:
            atual.set_fechado()

    return False
