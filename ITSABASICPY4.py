starhr,starmin=map(int,input().split())
endhr,endmin=map(int,input().split())
if endhr<=starhr and endmin<starmin:
    total=int(endhr*60+endmin)-(starhr*60+(60-starmin)+720)
else:
    total=int(endhr*60+endmin)-(starhr*60+(60-starmin))
hr=int(total/60)
if hr!=0:
    if total%60!=0:
        hr=hr+1
        total=int(total/30)
if hr==0:
    print(0)
elif hr<=2:
    print(total*30)
elif hr>2 and hr<=4:
    print((4*30)+((total-4)*40))
elif hr>4:
    print((4*30)+(4*40)+((total-8)*60))