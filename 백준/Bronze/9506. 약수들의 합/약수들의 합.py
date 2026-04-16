n=int(input())
while n!=-1:
    if n==-1:
        break
    arr=[]
    for i in range(1,n//2+1):
        if n%i==0:
            arr.append(i)
    if sum(arr)==n:
        print(f'{n} = ',end='')
        print(' + '.join(list(map(str, arr))))
    else:
        print(f'{n} is NOT perfect.')
    n=int(input())