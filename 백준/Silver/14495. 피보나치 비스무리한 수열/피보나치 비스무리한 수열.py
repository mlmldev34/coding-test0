def fibo(n):
    f=1
    l=1
    j=1
    if n<=3:
        return 1
    else:
        for k in range(n-3):
            temp=l
            temp2=j
            j=j+f
            f=temp
            l=temp2
        return j
n=int(input())
print(fibo(n))