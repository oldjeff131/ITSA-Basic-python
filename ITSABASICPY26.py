num=int(input())
N=[0]*num
M=[0]*num
N=input().split()
total=0
for i in range(0,num,1):
    for o in range(0,4,1):
        total=total+int(N[i][o])
    M[i]=total
    total=0
for i in range(0,num,1):
    for o in range(i+1,num,1):
        if M[i]>M[o]:
            change=M[o]
            M[o]=M[i]
            M[i]=change
            change=N[o]
            N[o]=N[i]
            N[i]=change
        if M[i]==M[o]:
            if N[i]>N[o]:
                change=M[o]
                M[o]=M[i]
                M[i]=change
                change=N[o]
                N[o]=N[i]
                N[i]=change
for i in range(0,num):
    if i<num-1:
        print(N[i],end=' ')
    else:
        print(N[i])
