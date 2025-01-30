#Highly Divisible Triangular Number

def memoize(func):
    table = [0,0,[2]]
    def helper(n):
        if n == len(table):
            table.append(func(n))
        return table[n]
    return helper

#store primes
def primeFactors():
    primes = [2]
    @memoize
    def factors(num):
        for prime in primes:
            if prime ** 2 > num:
                primes.append(num)
                return [num]
            else:
                if not num % prime:
                    return [prime] + factors(num//prime)

    i = 3

    while True:
        yield factors(i)
        i += 1




i = 0
old = 1
for factors in primeFactors():
    
    
    f = []
    current = factors[0]
    count = 0
    for factor in factors:
        if factor == current:
            count += 1
        else:
            if current == 2:
                count -= 1
            f.append(count+1)
            count = 1
            current = factor
    if current == 2:
        count -= 1
    f.append(count+1)
    prod = 1
    for num in f:
        prod *= num
    rtn = prod * old
    old = prod
    if rtn > 500:
        print(rtn)
        print(((i+2) * (i+3))//2)
        break
    i += 1

