#Smallest Multiple

def greatestCommonFactor(a,b):
    while True:
        r = a % b
        if r == 0:
            return b
        a = b 
        b = r



def smallestMultiple(max):
    i = max
    rtn = 1
    while i >= 1:
        r = greatestCommonFactor(rtn,i)
        rtn *= (i // r) 
        i -= 1
    return rtn


print(smallestMultiple(20))

