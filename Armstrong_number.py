n = 153
num = n
no_of_digits = len(str(n))                  # count number of Digits in n which is  3 
total = 0                                   # add total after a loop 
while num > 0:         
    ld = num % 10                           
    total = total + (ld ** no_of_digits)    # total = 0 + (3 ** 3)
    num = num // 10                         
    print(num, ld, total)                   # after one loop 15  3  27 
if total == n:                              # 153 is total (27 + 125 + 1) == n which is 153
    print("number is Armstrong")
else: 
    print("not Armstrong")