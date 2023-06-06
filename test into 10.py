def f(string, a):
    m = 0
    for n in range(len(string)):
        m += int(string[n]) * (a**(len(string) - n - 1))
    return m
print(f('11',2))