def fibo(n):
    f=1
    l=1
    arr=[]
    for i in range(n*2):
        if f>n:
            break
        arr.append(f)
        temp=l
        l+=f
        f=temp
    return arr
n=int(input())
for _ in range(n):
    num=int(input())
    result=[]
    arr=fibo(num)
    for j in reversed(arr):
        if num==0:
            break
        if num>=j:
            num-=j
            result.append(j)
    print(' '.join(list(map(str, reversed(result)))))