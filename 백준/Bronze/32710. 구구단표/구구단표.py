n = int(input())
r = 0
for i in range(1, 10):
    for j in range(1, 10):
        if n == i*j:
            r = 1
            break
print(r)
