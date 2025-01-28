#Summation of Primes

def isPrime(num,primes):
    for prime in primes:
        if num % prime == 0:
            return False
    return True

def PrimesBelow(n):
    primes = [2]
    a = 3
    while a <n:
        if isPrime(a,primes):
            primes.append(a)
        a += 2
    return primes

print(sum(PrimesBelow(2000000)))