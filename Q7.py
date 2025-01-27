#10001st Prime

def isPrime(num,primes):
    for prime in primes:
        if num % prime == 0:
            return False
    return True

def Prime(n):
    primes = [2]
    i = 1
    a = 3
    while i <n:
        if isPrime(a,primes):
            primes.append(a)
            i += 1
        a += 2
    return primes[-1]

print(Prime(10001))
        

