counter = 0
def func():
    global counter 
    if counter != 4:     # set a counter that function don't call when value is 4
        counter += 1     # incriment counter
        print(counter)   
        print("LG")
        func()           # if condition is true then the function recall 
    else:
        return           # if it is false it end the loop 
func()

''' func() called, counter=0
  → counter becomes 1
  → calls func() again (counter=1)
    → counter becomes 2
    → calls func() again (counter=2)
      → counter becomes 3
      → calls func() again (counter=3)
        → counter becomes 4
        → calls func() again (counter=4)
          → BASE CASE: counter==4, returns immediately
        ← prints "LG" (unwinding)
      ← prints "LG" (unwinding)
    ← prints "LG" (unwinding)
  ← prints "LG" (unwinding) '''

counter = 0
def func():
    global counter
    if counter == 4:
        return
    counter += 1
    func()
    print("LG")

func()