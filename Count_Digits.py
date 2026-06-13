from math import *             # Method 1
def countDigit(num):           # Value of Log10(6541) = 3.815644 near 4 
    return int(log10(num) + 1)

number = countDigit(6541)
print(number)

n = 45837                      # Method 2
num = n                       # 45837 // 10 remainder 7 and count = 1 
count = 0                     # n = 4583 // 10 remainder 3 and again count increase 2 and untill n == 0 
while num > 0:
    count += 1
    num = num // 10
    print(num, count)
