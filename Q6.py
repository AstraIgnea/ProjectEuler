#Sum Square Difference

def SumSquareDifference(max):
    squares = 0
    nums = 0
    i = 0
    while i <= max:
        squares += i ** 2
        nums += i
        i += 1
    return nums**2 - squares

print(SumSquareDifference(100))