# Brute Force
# num = int(input("Enter a number to find factor: "))
num = 20
result = []
for i in range (1,num+1):                              # have to ittrate all the numbeer to check the factor TC = O(n)
   if num % i == 0:                                    # SC = O(k) K -> could be total number of factors 
     result.append(i)

print(result)

# Better Solution 
num = 20 
result = []
for i in range (1, (num//2)+1):                        # after half of the number ittrate first then skip all the remaning and print the num at last 
    if num % i == 0:                                   # TC = O(n/2) = O(n) SC = O(k)
       result.append(i)
       
result.append(num)       
print(result)

# Optimal solution 
num = 36
result = []
i = 1
while i * i <= num:                                    # square the value of i and check it's square is less then or equals to square value 
   if num % i == 0:                                    
      result.append(i) 
      if num // i != i:                                # To avoide duplicate values  
         result.append(num // i)                       # TC = O(√n) + O(n logn) SC = O(k)
   i += 1
result.sort()
print(result)