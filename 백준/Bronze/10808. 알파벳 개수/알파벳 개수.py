s = list(input())
for i in [chr(97+j) for j in range(26)]:
    print(s.count(i), end=' ')