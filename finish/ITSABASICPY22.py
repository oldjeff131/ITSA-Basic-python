box=[[0]*3 for _ in range(3)]
R,L,S=0,0,0
ans=0
for x in range(0,3,1):
    box[x][0],box[x][1],box[x][2]=input().split()
for x in range(0,3,1):
    for y in range(0,3,1):
        R=R+int(box[x][y])
        L=L+int(box[y][x])
        S=S+int(box[2-y][y])
    if R==0 or R==3 or L==0 or L==3 or S==0 or S==3:
        ans=1
    R,L,S=0,0,0
for x in range(0,3,1):
    S=S+int(box[x][x])
if S==0 or S==3:
    ans=1
if ans==1:
    print("True")
else:
    print("False")
