a=['a', 'e', 'i', 'o', 'u']
s=''
r=0
while s!='#':
    r=0
    s=input()
    if s=='#':
        break
    s=s.replace(' ','')
    for i in s:
        if i.isalpha():
            i=i.lower()
            if i in a:
                r+=1
    print(r)