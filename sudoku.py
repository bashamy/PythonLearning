import numpy as np
sudokuinp1 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 1, 6, 0],
    [0, 6, 7, 0, 3, 5, 0, 0, 4],
    [6, 0, 8, 1, 2, 0, 9, 0, 0],
    [0, 9, 0, 0, 8, 0, 0, 3, 0],
    [0, 0, 2, 0, 7, 9, 8, 0, 6],
    [8, 0, 0, 6, 9, 0, 3, 5, 0],
    [0, 2, 6, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
])
sudokuinp2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
sudokuinp3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def possible (y,x,n,sudinp):
    for i in range(0,9):
        if sudinp[y][i] == n:
            return False
    for i in range(0,9):
        if sudinp[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudinp[y0+i][x0+j] == n:
                return False
    return True

def sudokuSolve(sudinp):
    for y in range(9):
        for x in range(9):
            if sudinp[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n,sudinp):
                        sudinp[y][x] = n
                        sudokuSolve(sudinp)
                        sudinp[y][x] = 0
                return
    print(np.matrix(sudinp))
    input("More?")

sudokuSolve(sudokuinp1)