n,d=map(int, input().split())
di1={
    'd':'q',
    'b':'p',
    'q':'d',
    'p':'b'
}
di2={
    'd':'b',
    'b':'d',
    'p':'q',
    'q':'p'
}
for i in range(n):
    a=list(input())
    for j in a:
        if d==1:
            print(di1[j],end='')
        else:
            print(di2[j],end='')
    if i<n-1:
        print()