starhr,starmin=map(int,input().split()) 
endhr,endmin=map(int,input().split()) 
if starhr==endhr:
    totaltime=int(endmin-starmin)
else:
    totaltime=int(endhr*60+endmin)-(starhr*60+starmin) 
hr=totaltime//60
if totaltime%60!=0:
    hr+=1
total=totaltime//30
if hr>4: 
    print((4*30)+(4*40)+((total-8)*60))  
elif hr>2 and hr<=4: 
    print((4*30)+((total-4)*40)) 
elif hr<=2: 
    print(total*30)
