step = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', ' ']

p, w = map(int, input().split())
s = input()
r = 0
e = 0
t = 0
b = 0
k = 0

for i in list(s):
    k += 1
    for j in range(len(step)):
        if i in step[j]:
            if i == ' ':
                t += 1
                if t >= 2:
                    b = 0
                    t = 1
                else:
                    b = 1
            else:
                t = 0
                b = 1
            if k > 1:
                if b == 1 and e == j:
                    r += w
                    e = j
                elif b == 1 and e != j:
                    e = j
            r += (step[j].index(i)+1)*p
            e = j

print(r)