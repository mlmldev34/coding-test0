x,y,w,h=map(int,input().split())
p=[abs(x),abs(y),abs(x-w),abs(y-h)]
print(min(p))