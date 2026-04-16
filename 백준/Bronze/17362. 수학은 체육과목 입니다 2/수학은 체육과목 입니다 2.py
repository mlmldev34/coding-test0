n=int(input())-1
print(5-n%4 if (n//4)%2 else n%4+1)