en=input().split()
for i in range(0,len(en)):
    en[i]=en[i].lower()
print(en)
a=len(en)
for i in range (0,len(en),1):
    for x in range(i+1,a,1):
        print(en,len(en),a,i,x)
        if x<=len(en):
            if en[i]==en[x]:
                del en[x]
                a=a-1
for i in range(0,len(en)):
    print(en[i],end=' ')