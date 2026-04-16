# 0.25 0.1 0.05 0.01

n=int(input())
arr=[]
for i in range(n):
    arr=[]
    c=int(input())
    s=c
    arr.append(s//25)
    s=s%25
    arr.append(s//10)
    s=s%10
    arr.append(s//5)
    s=s%5
    arr.append(s)
    print(' '.join(list(map(str, arr))))