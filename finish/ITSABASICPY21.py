num1=input().split()
big=float(max(num1))
small=float(min(num1))
print('maximum:%.2F\nminimum:%.2f'%(big,small))


# num1=input().split()
# for i in range (0,len(num1),1):
#     if i==0:
#         big,small=float(num1[i]),float(num1[i])
#     else:
#         if big<float(num1[i]):
#             big=float(num1[i])
#         if small>float(num1[i]):
#             small=float(num1[i])
# print('maximum:%.2F\nminimum:%.2f'%(big,small))
