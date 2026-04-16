n=int(input())
s=[]
for i in range(n):
    a=input()
    s.append(a.count('for')+a.count('while'))
print(max(s))