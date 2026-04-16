n = int(input())
r = []
for i in range(n):
    t = [0,0,0,0,0,0]
    a = list(map(int, input().split()))
    for i in range(6):
        if i+1 in a:
            t[i] += a.count(i+1)
    if max(t) == 3:
        r.append(10000+(t.index(3)+1)*1000)
    elif max(t) == 2:
        r.append(1000+(t.index(2)+1)*100)
    else:
        r.append(max(a)*100)
print(max(r))