import sys
n=int(sys.stdin.readline())
[print(i) for i in sorted([int(sys.stdin.readline().strip()) for i in range(n)])]