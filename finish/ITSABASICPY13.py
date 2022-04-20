suits = {'C' : 1, 'D' : 2, 'H' : 3, 'S' : 4} 
val = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, '11' : 11, '12' : 12, '13' : 13} 

n = int(input()) 
a = [] 
for i in range(n): 
    a = input().split()
    ls = sorted(a, key= lambda c: (suits[c[0]], val[c[1:]]), reverse=True) 
    print(' '.join(ls))  