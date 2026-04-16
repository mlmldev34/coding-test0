t=int(input())
for i in range(t):
    n=int(input())
    a=list(input())
    while 'ABB' in ''.join(a):
        k=''.join(a).find('ABB')
        a[k:k+3]=''
        a.insert(k,'B')
        a.insert(k+1,'A')
    print(''.join(a))