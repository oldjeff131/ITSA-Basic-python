def fk(n):
    n=int(n)
    if n==0 or n==1:
        return n+1
    elif n>1:
        return fk(n-1)+fk(n/2)
num=input()
print(fk(num))