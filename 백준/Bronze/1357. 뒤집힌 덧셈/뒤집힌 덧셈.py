def rev(x):
  return ''.join(list(reversed(str(x))))
a,b=map(int,input().split())
print(int(rev(int(rev(a))+int(rev(b)))))