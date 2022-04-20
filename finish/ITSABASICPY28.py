h = []
for _ in range(4):
    s = input()
    h.append(s)
n = input()
n = int(n)
m = [0, 0, 0, 0, 0, 0, 0]
h1, h2, h3 = h[1], h[2], h[3]
s1 = 0
for i in range(n):
    s = input()
    if(s == h[0]):
        # 特獎為8 位數號碼與特獎號碼相同者，獎金 200 萬元
        m[0] += 1
        s1 += 2000000
        continue
    elif(s == h[1] or s == h[2] or s == h[3]):
        # 頭獎為8 位數號碼與頭獎號碼相同者，獎金 20 萬元
        m[1] += 1
        s1 += 200000
        continue
    elif(s[1:] == h1[1:] or s[1:] == h2[1:] or s[1:] == h3[1:]):
        # 二獎為末 7 位數號碼與頭獎中獎號碼末 7 位相同者，各得獎金 4 萬元
        m[2] += 1
        s1 += 40000
        continue
    elif(s[2:] == h1[2:] or s[2:] == h2[2:] or s[2:] == h3[2:]):
        # 三獎為末 6 位數號碼與頭獎中獎號碼末 6 位相同者，各得獎金 1 萬元
        m[3] += 1
        s1 += 10000
        continue
    elif(s[3:] == h1[3:] or s[3:] == h2[3:] or s[3:] == h3[3:]):
        # 四獎為末 5 位數號碼與頭獎中獎號碼末 5 位相同者，各得獎金 4 千元
        m[4] += 1
        s1 += 4000
        continue
    elif(s[4:] == h1[4:] or s[4:] == h2[4:] or s[4:] == h3[4:]):
        # 五獎為末 4 位數號碼與頭獎中獎號碼末 4 位相同者各得獎金 1 千元
        m[5] += 1
        s1 += 1000
        continue
    elif(s[5:] == h1[5:] or s[5:] == h2[5:] or s[5:] == h3[5:]):
        # 六獎為末 3 位數號碼與頭獎中獎號碼末 3 位相同者各得獎金 2 百元
        m[6] += 1
        s1 += 200
        continue
for i, e in enumerate(m):
    if i != len(m) - 1:
        print(str(e), end=" ")
    else:
        print(str(e))
print(s1)