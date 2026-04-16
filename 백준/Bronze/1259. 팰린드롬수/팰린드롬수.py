while True:
  n=input()
  x=len(n)
  if n=='0':
    break
  if x%2==0:
    print('yes' if n[0:x//2]==''.join(list(reversed(n[x//2:]))) else 'no')
  else:
    print('yes' if n[0:x//2]==''.join(list(reversed(n[x//2+1:]))) else 'no')