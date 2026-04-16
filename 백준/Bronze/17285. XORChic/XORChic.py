t=input()
s='CHICKENS'
l=[]
for i in range(60):
    if ord(t[0])^i==ord(s[0]):
        key = i
        break
for k in t:
    l.append(chr(ord(k)^key))
print(''.join(l))