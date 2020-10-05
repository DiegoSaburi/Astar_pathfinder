import pygame
import math
from queue import PriorityQueue
from globals import *

class Quadrado:
    def __init__(self, linha, coluna, lado, total_rows):
        '''
        Menor unidade de medida do nosso quadro
        '''
        self.linha = linha
        self.coluna = coluna
        self.lado = lado
        self.total_rows = total_rows
        self.x = self.linha * self.lado
        self.y = self.coluna * self.lado
        self.cor = WHITE
        self.vizinhos = []
        self.total_rows = total_rows

    def get_pos(self):
        '''
        retorna: Tupla
        '''
        return self.linha, self.coluna
    def reset(self):
        '''
        Coloca o quadrado como sendo um quadrado a ser preenchido novamente
        '''
        self.cor = WHITE
    def eh_fechado (self):
        '''
        Retorna True se o quadrado ja foi "visitado"
        pelo menos uma unica vez
        retorna: Bool
        '''
        return self.cor == RED
    def update_vizinhos(self,grid):
        '''
        Checkará a presença de vizinhos (quadrados abertos para encontrar o caminho)
        '''
        if( (self.linha < self.total_rows - 1) and not grid[self.linha+1][self.coluna].eh_barreira() ):
            #Checkando presença abaixo
            self.vizinhos.append(grid[self.linha + 1 ][self.coluna])

        if((self.linha > 0 ) and not grid[self.linha - 1][self.coluna].eh_barreira()):
            #checkando presença acima
            self.vizinhos.append(grid[self.linha - 1 ][self.coluna])

        if((self.coluna < self.total_rows - 1) and not grid[self.linha][self.coluna + 1].eh_barreira()):
            #checkando presença na direita
            self.vizinhos.append(grid[self.linha][self.coluna + 1])

        if((self.coluna > 0) and not grid[self.linha][self.coluna - 1].eh_barreira()):
            #checkando presença na esquerda
            self.vizinhos.append(grid[self.linha][self.coluna - 1])

    def eh_aberto (self):
        '''
        Retorna True se o quadrado vizinho n foi "visitado" ainda
        retorna: Bool
        '''
        return self.cor == GREEN
    
    def eh_barreira(self):
        '''
        Retorna True se o quadrado for uma barreira
        retorna: bool
        '''

        return self.cor == BLACK
    
    def eh_inicio(self):
        '''
        Retorna true se o quadrado for o inicio do path
        retorna: Bool
        '''
        return self.cor == ORANGE

    def eh_fim(self):
        '''
        Retorna true se o quadrado for fim do path
        retorna: Bool
        '''
        return self.cor == TURQUOISE
    
    def set_fechado (self):
        '''
        Seta o quadrado como visitado
        '''
        self.cor = RED
    
    def set_aberto (self):
        '''
        Seta o quadrado como aberto
        '''
        self.cor = GREEN
    
    def set_barreira(self):
        '''
        Seta o quadrado como barreira
        '''

        self.cor = BLACK
    
    def set_inicio(self):
        '''
        Seta o quadrado como inicio
        '''
        self.cor = ORANGE
    def set_fim(self):
        '''
        Seta o quadrado como fim
        '''
        self.cor =  TURQUOISE
    def set_path(self):
        '''
        Seta o quadrado como path
        '''
        self.cor = PURPLE

    def desenhar(self, window):
        pygame.draw.rect(window, self.cor, (self.x, self.y, self.lado, self.lado))
    
    