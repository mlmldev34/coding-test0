n=int(input())
s=int((1+(8*n-7)**0.5)/2)
k1=((s-1)*s)//2
print(s-n+k1+1,n-k1)