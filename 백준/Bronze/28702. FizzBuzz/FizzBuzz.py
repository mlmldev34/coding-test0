def f(n):
    if n%15==0:
        return 'FizzBuzz'
    elif n%3==0 and n%5!=0:
        return 'Fizz'
    elif n%3!=0 and n%5==0:
        return 'Buzz'
    else:
        return int(n)

n1=input()
n2=input()
n3=input()

a=[n1,n2,n3]
p=[]

for i in a:
    if i=='FizzBuzz':
        p.append('15')
    elif i=='Fizz':
        p.append('3')
    elif i=='Buzz':
        p.append('5')
    else:
        p.append(int(i))
o=0
for i in range(3):
    if isinstance(p[i], int):
        o+=1
        print(f(p[i]+3-i))
        break
if o==0:
    print('Fizz')
