for i in range(2,40):
    s=''
    x=39
    n=i
    while x!=0:
        s+=str(x%n)
        x//=n
    s=s[::-1]
    if s[-1:]=='3':
        print(i) 
        #answer:4,6,9,12,18,36   