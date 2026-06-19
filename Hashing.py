'''
Constraints
1) 1 <= n[i] <= 10
2) n and m can have 10^8 elements 
'''
#Brutal
n = [5,3,2,2,1,5,5,7,5,10]        # j is pivot element 
m = [10,111,1,9,5,67,2]           # i is pivot element 

for i in m:                        
    count = 0                     # starting from 0th element in m as more element are found in n counter increas of that element if can't find and so cout 0 
    for j in n:                   
        if j == i:                # if element in n is found in m then the value of the counter get +1
            count += 1            # TC = O(m*n) = 10^8 * 10^8 = 10^16  SC = O(1)
    print(count)

#Optimal
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
hash_table = [0]*11               # make a hash list of 11 element and each index contain 0 by default

for num in n:                     
    hash_table[num] += 1          # increase the element index number as count increase 

for num in m:
    if 0 <= num < len(hash_table):# number must be in 1 to 10
        print(hash_table[num])    # if present print table if not then 0
    else:
        print(0)

#Dictionary
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
Dict = {}
for i in range (0, len(n)):     # TC O(n+m) SC O(n)
    if n[i] in Dict:
        Dict[n[i]] += 1
    else:
        Dict[n[i]] = 1
for j in range (0, len(m)):
    if m[j] in Dict:
        print(m[j], Dict[m[j]])


