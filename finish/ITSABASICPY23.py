money,a1,a2,a3=map(int,input().split(','))
total=money-(a1*15+a2*20+a3*30)
if total<0:
    print(0)
else:
    if total%50!=0:
        D50=int(total/50)
        total=total-(int(total/50)*50)
        if total%5!=0:
            D5=int(total/5)
            D1=total-(int(total/5)*5)
        else:
            D5=int(total/5)
            D1=0
    else:
        D50=int(total/50)
        D5,D1=0,0
    print('%d,%d,%d'%(D1,D5,D50))
