num1=input().split()
print(len(num1))
for i in range (0,len(num1),1):
    if i==0:
        big,small=float(num1[i]),float(num1[i])
    else:
        print(big,small)
        if big<float(num1[i]):
            big=float(num1[i])
        if small>float(num1[i]):
            small=float(num1[i])
print('maximum:%.2F\nminimum:%.2f'%(big,small))
