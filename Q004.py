#Largest Palindrome Product

def CheckPalindrome(num):
    num = str(num)
    mid = len(num) // 2
    i = 0
    while i < mid:
        if num[i] != num[-(i+1)]:
            return False
        i += 1
    return True

def LargestPalindromeProduct(digits):

    max = int("".join(["9" for a in range(digits)]))
    j = max
    i = max
    min = int("".join(["1" for a in range(digits)]))
    curr = 0
    while i >= min and j >= min :

        num = i * j

        if CheckPalindrome(num):
            if curr < num:
                curr = num
            
        if j == i:
            j = max
            i -= 1
        else:
            j -= 1

    return curr



print(LargestPalindromeProduct(3))
    