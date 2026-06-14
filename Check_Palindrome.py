n = int(input("Enter a number to check whether number is palindrome: "))
num = n                             # lets assume n = 5413
counter = 0                         # Checking whether number is palinedrome or not
while num > 0:                      # in counter the last digit if n is become the first of counter 
    LD = num % 10                   # 5413 % 10 = 541.3 so Last Digit is 3
    counter = (counter*10) + LD     # counter = (counter current value which is 0 now * 10) + 3
    num = num // 10                 # num = 5413 // 10 = 541  
                                    # num = 541 and counter = 3
if  n == counter:                   # when n == 0 counter = 3145
    print("true")                   # 1st condition false 
else :                              # 2nd condition true 
    print("false")