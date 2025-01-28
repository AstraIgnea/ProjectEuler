#Largest Product in a Grid

def horizontalSearch(grid):
    i = 0
    j = 0
    max = 0
    while j <= 19:
        while i <= 16:
            prod = int(grid[j][i]) * int(grid[j][i+1]) * int(grid[j][i+2]) * int(grid[j][i+3])
            if prod > max:
                max = prod
            i+=1
        i = 0
        j += 1
    return(prod)

def verticalSearch(grid):
    i = 0
    j = 0
    max = 0
    while j <= 19:
        while i <= 16:
            prod = int(grid[i][j]) * int(grid[i+1][j]) * int(grid[i+2][j]) * int(grid[i+3][j])
            if prod > max:
                max = prod
            i+=1
        i = 0
        j += 1
    return(prod)

def lrDiagonalSearch(grid):
    i = 0
    j = 0
    max = 0
    while j <= 16:
        while i <= 16:
            prod = int(grid[i][j]) * int(grid[i+1][j+1]) * int(grid[i+2][j+2]) * int(grid[i+3][j+3])
            if prod > max:
                max = prod
            i += 1
        i = 0
        j += 1
    return max

def rlDiagonalSearch(grid):
    i = 3
    j = 0
    max = 0
    while j <= 16:
        while i <= 19:
            prod = int(grid[i][j]) * int(grid[i-1][j+1]) * int(grid[i-2][j+2]) * int(grid[i-3][j+3])
            if prod > max:
                max = prod
            i += 1
        i = 3
        j += 1
    return max

def search(grid):
    h = horizontalSearch(grid)
    v = verticalSearch(grid)
    l = lrDiagonalSearch(grid)
    r = rlDiagonalSearch(grid)
    return(max([h,v,l,r]))

file = open ("Q11","r")
grid = [line.split(" ") for line in file.read().split("\n")]
for line in grid:
    print(line)

print(search(grid))

