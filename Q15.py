#Lattice Paths
import math

def pathsInGridNxN(n):
    return math.factorial(n * 2) // (math.factorial(n) ** 2)

print(pathsInGridNxN(20))