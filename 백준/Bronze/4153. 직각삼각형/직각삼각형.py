while True:
  p=list(sorted(list(map(int, input().split()))))
  if p[0]==0:
    break
  if p[0]**2+p[1]**2==p[2]**2:
    print("right")
  else:
    print('wrong')