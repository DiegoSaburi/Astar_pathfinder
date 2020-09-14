from objects import *
from globals import *
def h(p1,p2):
    '''
    Retorna a distancia entre os pontos p1 e p2
    retorna: float
    '''
    x1,y1 = p1
    x2,y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)
def make_grid (linhas,largura):
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

def draw_grid (window, linha, largura):
    '''
    Desenhará as linhas do grid
    '''
    gap = largura//linha
    for i in range(linha):
        pygame.draw(window, GREY, (0 , i * gap) , (largura , i*gap)) #denha as linhas horizontais
        for j in range(linha):
            pygame.draw(window, GREY, ( j* gap , 0 ), (j*gap , largura)) #desenha as linhas verticais

def draw(window, grid, linha, largura):

    window.fill(WHITE) #irá pintar toda a window de branco

    for linha in grid:
        for quad in linha:
            quad.desenhar(window) #irá desenhar os quadrados da grid
    
    draw_grid(window, linha, largura)
    pygame.display.update()

def get_click_pos(pos, linha, largura):
    gap = largura // linha
    y,x = pos

    linha = y // gap
    coluna = x//gap

    return linha,coluna
