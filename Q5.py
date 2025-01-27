#Smallest Multiple



def smallestMultiple(max):
    i = 1
    rtn = 1
    while i <= max:
        r = rtn % i #the remainder of out current multiple divided by the number we have gotten to
        
        if r != 0:  #If the remainder is 0 then the number fits inside out current multiple
            if i % r != 0:  # For the multiple to contain the number you must take the same action as you would to make the remainder a multiple.
                rtn *= i          #If the remainder is not a factor of the number, we must multiply by the number, since the number is a new prime
            else:
                missing = i // r  #If the remainder is a factor of the number, you can multiply the remainder to equal the number
                rtn *= missing
        i += 1
    return rtn


print(smallestMultiple(20))

