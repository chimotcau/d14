def f(string, a):
    m = 0
    for n in range(len(string)):
        m += int(string[n]) * (a**(len(string) - n - 1))
    return m
for x in range(6,10):
    for y in range(6,10):
        if f('225',x) ==f('405',y):
            print(x,y)
            #answer:8  

