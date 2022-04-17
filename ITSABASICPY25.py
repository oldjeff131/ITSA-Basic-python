num=int(input())
total=0
for x in range(0,num+1,1):
    a=list(input())
    for i in a:
        total=total+(ord(i))
print(str(total)+"\n")