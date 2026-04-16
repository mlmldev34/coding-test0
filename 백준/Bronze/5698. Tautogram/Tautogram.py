while True:
    a=input()
    if a=='*':
        break
    l=a.split()
    k=l[0][0].lower()
    print(['N','Y'][''.join([i[0].lower() for i in l])==k*len(l)])