n = 5473
num = n
while num > 0 :              
    last_digit = num % 10    # save the last digit of the number which if 3 first 
    num  = num // 10         # remove number one by one 
    print(num, last_digit)   # Extractind digits
