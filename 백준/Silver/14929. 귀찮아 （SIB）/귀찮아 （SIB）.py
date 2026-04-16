n = int(input())
a = list(map(int, input().split()))
r = 0
s = sum(a)

for i in a:
    r += i*(s-i)
print(r//2)