n = int(input())
arr = []
for i in range(n):
    arr.append(input())
brr = list(sorted(list(set(arr))))
count = [0]*len(brr)
for i in arr:
    for j in brr:
        if i==j:
            count[brr.index(j)]+=1
print(brr[count.index(max(count))])