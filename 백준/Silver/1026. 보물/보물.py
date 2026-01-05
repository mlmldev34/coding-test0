n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
print(sum([list(sorted(a))[i]*list(sorted(b,reverse=True))[i] for i in range(n)]))