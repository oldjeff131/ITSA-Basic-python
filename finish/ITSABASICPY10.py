n,m=map(int,input().split())
while m!=0:
    temp=m
    m=n%m
    n=temp
print(n)
