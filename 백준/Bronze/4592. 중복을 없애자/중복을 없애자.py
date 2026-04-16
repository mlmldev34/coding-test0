while True:
    l=input()
    if l=='0':
        break
    l=list(map(int,l.split()))[1:]
    t=0
    for i in l:
        if t==i:
            pass
        else:
            print(i,end=' ')
        t=i
    print('$')