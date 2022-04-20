def transpose(list1):  
    return [list(row) for row in zip(*list1)]  
  
x, y = input().split()  
a = []  
for i in range(0, int(x)):  
    a.append(list(map(int, input().rstrip().split())))  
ls = transpose(a)  
for matrix in ls:  
    print(' '.join(map(str, matrix))) 