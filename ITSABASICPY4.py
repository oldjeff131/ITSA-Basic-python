time=[0,0,0,0]
for x in range(4):
    time[x]=int(input())
total=int(time[2]*60+time[3])-(time[0]*60+time[1])
hr=total/60
if hr<=2:
    print(total/30)*20
elif hr>2 & hr<=4:
    print(total/30)*40
elif hr>4:
    print(total/30)*60