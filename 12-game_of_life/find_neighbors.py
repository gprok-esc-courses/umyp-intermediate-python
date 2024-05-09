import  random

def alive_neighbors(r, c, cur):
    n = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if i >= 0 and j >= 0 and i < ROWS and j < COLS:
                n += cur[i][j]
    n = n - cur[r][c]
    return n

gen = 0
ROWS = 6
COLS = 6

current = [[0]*COLS for i in range(ROWS)]
next = [[0]*COLS for i in range(ROWS)]

for row in range(ROWS):
    for col in range(COLS):
        probability = random.randint(1, 100)
        if probability > 60:
            current[row][col] = 1
        else:
            current[row][col] = 0

for row in range(ROWS):
    print(current[row])

for row in range(ROWS):
    for col in range(COLS):
        n = alive_neighbors(row, col, current)
        print(n, end=' ')
        if n < 2 or n > 3:
            next[row][col] = 0
        elif n == 3:
            next[row][col] = 1
        else:
            next[row][col] = current[row][col]
    print()

for row in range(ROWS):
    print(next[row])