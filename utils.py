def h(p1,p2):
    '''
    Retorna a distancia entre os pontos p1 e p2
    retorna: float
    '''
    x1,y1 = p1
    x2,y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)
