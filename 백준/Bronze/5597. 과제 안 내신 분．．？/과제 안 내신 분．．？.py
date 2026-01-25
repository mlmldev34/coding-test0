a=[]
for i in range(28):
    n=int(input())
    a.append(n)
for k in range(30):
    if not([j for j in range(1,31)][k] in a):
        print(k+1)
     