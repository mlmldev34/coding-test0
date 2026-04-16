x1,x2=map(int, input().split())
a,b,c,d,e=map(int, input().split())
A=(1/3)*a
B=0.5*(b-d)
C=(c-e)
print(int(A*(x2**3-x1**3)+B*(x2**2-x1**2)+C*(x2-x1)))