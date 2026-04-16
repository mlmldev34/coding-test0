n = int(input())
arr = []

for i in range(n):
    a, b = input().split()
    if a == 'ChongChong' or b == 'ChongChong' or a in arr or b in arr:
        arr.append(a)
        arr.append(b)
    
print(len(list(set(arr))))