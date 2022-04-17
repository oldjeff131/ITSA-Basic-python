money,a1,a2,a3=map(int,input().split())
total=a1*15+a2*20+a3*30
if total%50!=0:
    D50=int(total/50)
    total=total-int(total/50)
    if total%10!=0:
        D10=int(total/10)
        D1=total-int(total/10)
    else:
        D10=int(total/10)
        D1=0
else:
    D50=int(total/50)
    sad=56
    D10,D1=0
print(D1,D10,D50)