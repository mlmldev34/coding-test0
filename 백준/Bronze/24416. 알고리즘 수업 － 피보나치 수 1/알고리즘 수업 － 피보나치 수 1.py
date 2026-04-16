def fib(n,c):
    l=1
    k=1
    for i in range(3, n+1):
        temp=k
        k+=l
        l=temp
        c+=1
    return[k,c]

c=0
n=int(input())
print(' '.join(list(map(str, fib(n,c)))))