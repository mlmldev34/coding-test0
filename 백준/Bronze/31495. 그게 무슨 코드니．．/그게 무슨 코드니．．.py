s=input()
if s[0]=='\"' and s[-1]=='\"' and s[1:len(s)-1]!='':
    print(s[1:len(s)-1])
else:
    print("CE")