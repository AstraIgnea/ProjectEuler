#Special Pythagorean Triplet

def SPT(num):
    c = 998
    a = 1
    b = 1
    while c > 0:
        while b > 0:
            if a ** 2 + b ** 2 == c ** 2:
                return(a*b*c)
            b -= 1
            a += 1
        c -= 1
        b += a
        a = 1

print(SPT(1000))