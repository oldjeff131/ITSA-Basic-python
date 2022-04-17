a=list(input())
end=['0','0','0','0']
As,Bs,ends=0,0,0
while True:
    b=list(input())
    for i in range(0,len(a),1):
        if b[i]==end[i]:
            ends=ends+1
    if ends==4:
        break
    for i in range(0,len(b),1):
        if b[i]==a[i]:
            As=int(As+1)
        else:
            for x in range(0,len(a),1):
                if b[i]==a[x]:
                    Bs=int(Bs+1)
    print('%dA%dB'%(As, Bs))
    As,Bs=0,0
    