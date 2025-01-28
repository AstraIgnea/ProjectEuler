#Multiples of 3 or 5

i = 3
count = 0
while i < 1000:
    count += i
    i += 3

i = 5

while i < 1000:
    if i%3 != 0:
        count += i
    i += 5

print(count)