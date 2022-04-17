num=int(input())
if num<0:
    num+=256
a=bin(num)
a=a[2:]
print(a.zfill(8))
    
