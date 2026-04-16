w=input()
s=input()
l=[];r=[]
for i in w:
    if w.count(i)==1:
        l.append(i)
    else:
        if not(i in l):
            l.append(i)
for k in 'abcdefghijklmnopqrstuvwxyz'.upper():
    if len(l) > 26:
        break
    if not(k in l):
        l.append(k)
for j in s:
    r.append(l[ord(j)-65])
print(''.join(r))