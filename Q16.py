#Power Digit Sum

def powerDigitSum(base,power):
    num = str(base ** power)
    count = 0
    for char in num:
        count += int(char)
    return(count)

print(powerDigitSum(2,1000))