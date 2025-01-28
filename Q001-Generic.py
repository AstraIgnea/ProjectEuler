#Multiples of 3 or 5

def counter(factors,max):

    if factors == []:
        return 0
    
    i = 0
    count = counter(factors[1:],max)

    while i < max:
        
        unique = True
        for factor in factors[1:]:
            if i % factor == 0:
                unique = False
                break
        
        if unique:
            count += i

        i += factors[0]
        
        return (count)




print(counter([3,5],1000))