#Longest Collatz Sequence

def memoize(func):
    table = {}
    table[1] = 1
    def helper(n):
        if n not in table:
            table[n] = func(n)
        return table[n]
    return helper

@memoize
def collatzSequence(num):
    if num%2:
        return collatzSequence(3 * num + 1) + 1
    else:
        return collatzSequence(num // 2) + 1

def largestCollatz(num):
    max = [0,0]
    while num > 1:
        length = collatzSequence(num)
        if length > max[1]:
            print(num)
            max = [num,length]
        num -= 1
        
    return(max)

print(largestCollatz(1000000))