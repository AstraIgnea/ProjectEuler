#Maximum Path Sum I

file = open("Q018.txt","r")
pyramid = [[int(num) for num in line.split(" ")] for line in file.read().split("\n")]
i = len(pyramid) - 2
while i >= 0:
    

    j = len(pyramid[i]) - 1
    while j >= 0:
        if pyramid[i + 1][j] >= pyramid[i + 1][j + 1]:
            pyramid[i][j] += pyramid[i + 1][j]
        else:
            pyramid[i][j] += pyramid[i + 1][ j + 1]
        j -= 1
    i -= 1
print(pyramid[0])