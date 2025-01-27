#Largest Prime Factor

def LargestPrimeFactor(num):
    i = 2
    while i <= num:
        if i == num:
            return i
        
        if num % i == 0:
            num = num // i
        else:
            i += 1
        

print(LargestPrimeFactor(600851475143))