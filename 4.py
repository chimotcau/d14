for a in range(2,32):
    s=''
    n=a
    x=31
    while x!=0:
        s+=str(x%n)
        x//=n
    s=s[::-1]
    if s[-2:]=='11':
        print(a)
        #answer:2,3,5,20,30    