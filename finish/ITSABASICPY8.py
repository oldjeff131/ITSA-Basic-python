def isPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False
    return True

num=int(input())
if isPrime(num)==True:
    print("YES")
else:
    print("NO")


# a = int(input())
# if a > 1:
#     for i in range(2, int(a / 2) + 1):
#         if a%i == 0:
#             print("NO") 
#             break
#     else:
#         print("YES")
# else:
#     print("NO"