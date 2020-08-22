import numpy as np
grid1 = np.zeros((9, 9))
startnum = input("Enter start number of Sudoku (1-9): ")
c = int(startnum)
if c%9 == 0:
    c = 9
else:
    c = c%9

for a in range(9):
    for b in range(9):
        if a == 0:
            grid1[a][b] = c+b
            if grid1[a][b] > 9 :
                grid1[a][b] = grid1[a][b] - 9
        elif a > 0 and a%3 != 0:
            grid1[a][b] = grid1[a-1][b]+3
            if grid1[a][b] > 9 :
                grid1[a][b] = grid1[a][b] - 9
        elif a > 0 and a%3 == 0:
            grid1[a][b] = grid1[a-3][b]+1
            if grid1[a][b] > 9 :
                grid1[a][b] = grid1[a][b] - 9

print(np.matrix(grid1))