n, w, h = map(int, input().split())
ma = (w**2+h**2)**(0.5)
for i in range(n):
    m = int(input())
    if m <= ma:
        print("DA")
    else:
        print("NE")