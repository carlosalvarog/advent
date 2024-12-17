
def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
# Code here
    grid=list(map(lambda p: list(map(lambda p2:1 if p2 else 0, p )), grid))
    filaFalse = [0]*(len(grid[0])+2)
    g=[filaFalse]
    final = [[0] * len(grid[0]) for _ in range(len(grid))]
    print(final)

    for fila in grid:
        g.append([0]+fila+ [0])
    g.append(filaFalse)
    print(g)

    
    for fila  in range(1,(len(g)-1)):
        for columna in  range(1,(len(g[0])-1)):
           t:int=g[fila+1][columna]+ g[fila-1][columna]+g[fila][columna+1]+g[fila][columna-1]+g[fila+1][columna+1]+g[fila-1][columna-1]+g[fila+1][columna-1]+g[fila-1][columna+1]
           
           final[fila-1][columna-1]=t
    print(final)

detect_bombs([
  [True, True],
  [False, False],
  [True, True]
])

