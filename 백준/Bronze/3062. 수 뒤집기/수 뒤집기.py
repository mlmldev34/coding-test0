n=int(input())
for i in range(n):
    numA = list(input())
    numB = list(reversed(numA))
    numC = int(''.join(numA))+int(''.join(numB))
    if(list(str(numC)) == list(reversed(str(numC)))):
        print('YES')
    else:
        print('NO')