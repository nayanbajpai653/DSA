''' Print 1 to N using recursion '''
def func(i,n):
    for j in range(i):
        if j>n:
            return
    print(j)
    func(i+1, n)
func(1,4)
