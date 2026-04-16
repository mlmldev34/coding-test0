from collections import Counter
import sys

n=int(sys.stdin.readline())
arr=[int(sys.stdin.readline()) for i in range(n)]
print(round(sum(arr)/n))
print(list(sorted(arr))[n//2])

count = Counter(arr)
brr=count.most_common()
maximum = brr[0][1]
crr=[]
for i in brr:
    if i[1]==maximum:
        crr.append(i[0])
if len(crr)>=2:
    print(sorted(crr)[1])
else:
    print(crr[0])
print(max(arr)-min(arr))