a=list(input())
b=list(input())
check=0
total=0
for i in range(0,len(b)-len(a)+1,1):
    for x in range(0,len(a),1):
        if b[i+x]==a[x]:
            check=check+1
        else:
            check=0
        print(total,a,b,len(a),len(b),i,x,b[i+x]==a[x],check)
    if check==len(a):
        total=total+1
    check=0
print(total)

