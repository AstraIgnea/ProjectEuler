#Factorial Digit Sum

import math

factorial = math.factorial(100)
factorial = str(factorial)

count = 0
for char in factorial:
    count += int(char)

print(count)