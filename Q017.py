#Number Letter Counts

def counter(list):
    count = 0
    for num in list:
        count += len(num)
    return(count)

def ones():
    list = ["one","two","three","four","five","six","seven","eight","nine"]
    return(counter(list))

def tens():
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    ten = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    count = 0
    count += ones() * 9
    count += counter(teens)
    count += counter(ten) * 10
    return(count)

def hundreds():
    hundred = [len(item) for item in ["hundred","and"]]
    count = 0
    count += ones() * 100
    count += 9 * (100 * hundred[0] + 99 * hundred[1])
    count += 10 * tens()
    return (count)

count = 0
count += hundreds() + len("onethousand")
print(count)
    
    