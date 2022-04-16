num=int(input())
total=0
for i in range(1,num+1,1):
    if i%3==0:
        total=total+i
print(total)