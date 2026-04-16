import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dic = {}
for i in range(n):
    x = sys.stdin.readline().rstrip().split()
    dic[x[0]] = x[1]

for i in range(m):
    sys.stdout.write(dic[sys.stdin.readline().rstrip()]+'\n')