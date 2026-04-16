L = int(input())
R = int(input())
r = L
a = []
x = 0

while r > 5:
    r *= (R/100)
    r = int(r)
    a.append(r)

for i in range(len(a)):
    if a[i] > 5:
        x += 2**(i+1)*a[i]

print(x)