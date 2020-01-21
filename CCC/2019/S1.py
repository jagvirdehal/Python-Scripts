flips = list(input())
grid = [
    [1,2],
    [3,4]
]


def horizontal(g):
    gp = g[:]
    newGrid = [[0,0],[0,0]]
    newGrid[0][0] = gp[1][0]
    newGrid[1][0] = gp[0][0]
    newGrid[0][1] = gp[1][1]
    newGrid[1][1] = gp[0][1]
    return newGrid

def vertical(g):
    n = [[0,0],[0,0]]
    n[0][0] = g[0][1]
    n[0][1] = g[0][0]
    n[1][0] = g[1][1]
    n[1][1] = g[1][0]
    return n

for i in flips:
    if i == "H":
        grid = horizontal(grid)
    elif i == "V":
        grid = vertical(grid)

print(grid[0][0],grid[0][1])
print(grid[1][0],grid[1][1])