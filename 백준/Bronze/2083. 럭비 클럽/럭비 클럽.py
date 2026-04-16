a=''
while 1:
    a=input()
    if a=='# 0 0':
        break
    if int(a.split()[1])>17 or int(a.split()[2])>=80:
        print(a.split()[0], 'Senior')
    else:
        print(a.split()[0], 'Junior')