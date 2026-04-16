n=int(input())
for i in range(n):
    a,b=input().split()
    print("Distances: ",end='')
    for j in range(len(a)):
        if ord(b[j])>=ord(a[j]):
            print(ord(b[j])-ord(a[j]), end=' ')
        else:
            print(26+ord(b[j])-ord(a[j]), end=' ')
    print()