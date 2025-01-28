# Even Fibonacci Numbers

def EvenFib(max):
    a = 0
    b = 1
    count = 0
    while b < max:
        if b % 2 == 0:
            count += b
        temp = a + b
        a = b
        b = temp
    
    return count

print(EvenFib(4000000))