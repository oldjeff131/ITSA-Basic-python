num=int(input())
a=list(input())
total=0
for x in range(1,num+1,1):
    for i in a:
        total=total+(ord(i))
print(str(total)+"\n")