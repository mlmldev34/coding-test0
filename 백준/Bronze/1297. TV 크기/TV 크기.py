d,w,h=map(int,input().split())
a=d/((w**2+h**2)**(1/2))
print(int(w*a),int(h*a))