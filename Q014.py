#Longest Collatz Sequence

def collatzSequence(num):
    i = 1
    while num > 1:
        if num%2:
            num = 3 * num + 1
        else:
            num //= 2
        i += 1
    return i

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