x = input().lower()
print(len(x.split()))
d = {}
for i in x:
    if i not in ',. ':
        if i in d: d[i] += 1
        else: d[i] = 1

for r in sorted(d.items(), key = lambda v: ord(v[0])):
    print("%s : %d" %r)