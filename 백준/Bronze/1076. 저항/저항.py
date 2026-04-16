a=[['black',0,1],
['brown',1,10],
['red',2,100],
['orange',3,1000],
['yellow',4,10000],
['green',5,100000],
['blue',6,1000000],
['violet',7,10000000],
['grey',8,100000000],
['white',9,1000000000]]

s=''
p1=input()
p2=input()
p3=input()
for j in a:
  if p1 in j[0]:
    s+=str(j[1])
for j in a:
  if p2 in j[0]:
    s+=str(j[1])
for j in a:
  if p3 in j[0]:
    s=int(s)*j[2]
print(s)