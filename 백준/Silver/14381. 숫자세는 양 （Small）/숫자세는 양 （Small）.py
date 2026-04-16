n=int(input())
for i in range(1,n+1):
    arr=set()
    t=int(input())
    x=t
    if t==0:
        print(f'Case #{i}: INSOMNIA')
    else:
        while True:
            if len(arr)==10:
                print(f'Case #{i}: {t-x}')
                break
            arr=arr|set(list(map(int, list(str(t)))))
            t+=x