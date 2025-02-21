#Counting Sundays

def daysInMonth(year,month):
    month -= 1
    days30 = [8,3,5,10]

    while True:
        if month == 1:
            if(year % 4):
                yield(28,year)
            elif(year % 100):
                yield(29,year)
            elif(year % 400):
                yield(28,year)
            else:
                yield(29,year)
        elif month in days30:
            yield(30,year)
        else:
            yield(31,year)
        month += 1
        if month == 12:
            month = 0
            year += 1



    

generator = daysInMonth(1900,1)
days = 0

#Iterates through to the start date from the known monday
for i in range(0,12):
    (num,_) = next(generator)
    days += num 
    days %= 7

print(days)

#Counts the Sundays that occur
count = 0
for (num,year) in generator:
    if year > 2000:
        break
    days += num 
    days %= 7
    if days == 6:
        count += 1

print(count)