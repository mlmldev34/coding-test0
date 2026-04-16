a,b=map(int,input().split())
d=0
arr=[]
d=(a-a%b)/b
a%=b
print(int(d),end='.')
for i in range(1500):
    a*=10
    d=(a-a%b)/b
    a%=b
    print(int(d),end='')