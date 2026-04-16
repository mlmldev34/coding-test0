r=0

def m(a):
    if a%2==0:
        b1,b2=a//2,a//2
    else:
        b1,b2=a//2,a//2+1
    global r
    r+=b1*b2
    if b1>1:
        m(b1)
    if b2>1:
        m(b2)

n=int(input())
m(n)
print(r)