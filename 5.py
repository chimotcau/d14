count=0
for a in range(10,18):
    s=''
    x=a
    while x!=0:
        s+=str(x%5)
        x//=5
    s=s[::-1]
    n=s.count('2')
    count+=n
print(count)
#answer:7       
    
