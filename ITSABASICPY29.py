passnum=input()
a=list(passnum)
en=[['A',1,0],['B',1,1],['C',1,2],['D',1,3],['E',1,4],['F',1,5],['G',1,6],
    ['H',1,7],['I',3,4],['J',1,8],['K',1,9],['L',2,0],['M',2,1],['N',2,2],
    ['P',2,3],['Q',2,4],['R',2,5],['S',2,6],['T',2,7],['U',2,8],['V',2,9],
    ['X',3,0],['Y',3,1],['W',3,2],['Z',3,3],['O',3,5]]
for i in range (0,25):
    if a[0]==en[i][0]:
        X1=en[i][1]
        x2=en[i][2]
p=X1+(9*int(x2))
for i in range(1,10):
    if i<8:
        p=p+((9-i)*int(passnum[i]))
    else:
        p=p+int(passnum[i])
if p%10==0:
    print("CORRECT!!!")
else:
    print("WRONG!!!")