n=int(input())
t=0
for i in range(n):
    a=input()
    c=list(a)
    s=[]
    x=''
    for k in range(len(c)):
        if not(c[k] in s):
            s.append(c[k])
    for j in range(len(s)):
        x+=s[j]*c.count(s[j])
    if x==a:
        t+=1
print(t)