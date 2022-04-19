num=int(input())
time=input().split()
car=1
for i in range(0,num,2):
    if i>0:
        if time[i]<time[i-1]:
            car+=1
        for x in range(0,num,2):
            

