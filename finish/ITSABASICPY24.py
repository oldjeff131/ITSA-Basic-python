r=float(input())
n=int(input())
p=int(input())
total=0
for i in range(1, n+1):
    total=total+p
    add=total*r
    total=total+add
print(int(total))
