import sys

n = int(sys.stdin.readline())

dic = {}

for i in range(n):
    a = sys.stdin.readline().rstrip().split()
    if a[1]=='enter':
        dic[a[0]] = a[1]
    else:
        del dic[a[0]]
[print(i) for i in list(sorted(dic, reverse=True))]