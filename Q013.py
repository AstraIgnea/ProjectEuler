#Large Sum

file = open("Q013","r")
sum = 0
for line in file:
    sum += int(line)
print(str(sum)[0:10])