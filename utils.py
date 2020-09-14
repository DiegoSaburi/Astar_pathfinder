from objects import *

def h(p1,p2):
    '''
    Retorna a distancia entre os pontos p1 e p2
    retorna: float
    '''
    x1,y1 = p1
    x2,y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)
def make_grid (linhas,largura):
    grid = []
    gap = largura // linhas #tamanho da largura de cada cubo do grid
    for i in range(linhas):
        grid.append([])
        for j in range(linhas):
            quad = Quadrado(i,j, gap, linhas)
            grid[i].append(quad) #cada quadrado criado será adicionado na linha

    return grid

