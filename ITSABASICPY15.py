a=(input().split(" "or","or"."))
b=[]
for i in range (len(a)):
    a[i]=a[i].lower()
for i in range (len(a)):
    for x in range(len(a[i])):
        for y in range(97,123,1):
            if ord(a[i][x])==y:
                if len(b)!=0:
                    for z in range(0,len(b)):
                        if b[z][0]==a[i][x]:
                            total=int(b[z][1])
                            total+=1
                            b[z][1]=str(total)
                        else:
                            b.append('%s1'%(a[i][x]))
                else:
                    b.append('%s1'%(a[i][x]))
                break
print(len(a))
for i in range (len(b)):
    print('%s : %d'%(b[i][0],int(b[i][1])))
