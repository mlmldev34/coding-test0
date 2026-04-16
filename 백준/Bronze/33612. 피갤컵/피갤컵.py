y0,m0=divmod(8+int(input())*7-7,12)
if m0==0:
    m0=12
    y0-=1
print(2024+y0,m0)