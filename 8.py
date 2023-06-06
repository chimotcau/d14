for a in range(2,73):
    s=''
    x=71
    n=a
    while x!=0:
        s+=str(x%n)
        x//=n
    s=s[::-1]
    if s[-2:]=='13':
        print(a)    
