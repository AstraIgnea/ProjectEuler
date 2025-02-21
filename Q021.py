#Amicable Numbers

def memoize(func):
    table = [0,0,[2]]
    def helper(n):
        if n == len(table):
            table.append(func(n))
        return table[n]
    return helper

#store primes
def primeFactors():
    yield [2]
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

def Divisors(primes):
    divisors = [1]
    prev = primes[0]
    count = 0
    for prime in primes:

        if prime == prev:
            count+=1
        else:
            temp = divisors.copy()
            for i in range(1,count+1):

                divisors += [num * (prev**i) for num in temp]
            prev = prime
            count = 1
    temp = divisors.copy()
    for i in range(1,count+1):

        divisors += [num * (prev**i) for num in temp]
    return(divisors[:-1])

sumOfDivisors = [0,1]
i = 2
count = 0
for primes in primeFactors():

    total = sum(Divisors(primes))
    sumOfDivisors.append(total)
    if total < i:
        if sumOfDivisors[total] == i:
            count += total + i

    i+=1
    if i > 10000:
        break
print(count)






        

    



