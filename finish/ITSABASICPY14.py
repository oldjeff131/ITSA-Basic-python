a=list(input())
if len(a)%2==0:
    for i in range(0,int(len(a)/2),1):
        if a[i]!=a[len(a)-(i+1)]:
            print("NO")
            break
        elif i==len(a)/2-1:
            print("YES")
            break
else:
    for i in range(0,int(len(a)/2),1):
        if i!=len(a)/2:
            if a[i]!=a[len(a)-(i+1)]:
                print("NO")
                break
            elif i==int(len(a)/2-1):
                print("YES")
                break