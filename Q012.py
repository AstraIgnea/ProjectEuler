#Highly Divisible Triangular Number

def factors(num):
    i = 2
    count = 0
    while i <= num:
        if num % i:
            if count > 0:
                yield (i,count)
            count = 0
            i += 1
        else:
            num //= i
            count += 1
    if count > 0:
        yield (i,count)


def Divisors(num):
    divisors = [1]
    for factor in factors(num):
        (a,c) = factor
        temp = divisors.copy()
        for i in range(1,c+1):
            mul = a**i
            for div in temp:
                rtn = div * mul
                divisors.append(rtn)
    return(divisors)
        
def triangularNumber():
    total = 0
    i = 0
    while True:
        i += 1
        total += i
        yield total

def HighlyDivisibleTriangularNumber(divisors):
    for num in triangularNumber():
        if len(Divisors(num)) > divisors:
            return num
print(HighlyDivisibleTriangularNumber(500))
