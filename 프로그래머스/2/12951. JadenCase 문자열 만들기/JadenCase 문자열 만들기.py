def solution(s):
    a = ''
    m = 1
    for i in s:
        if m:
            a+=i.upper()
        else:
            a+=i.lower()
        if i == ' ':
            m = 1
        else:
            m = 0
    return a