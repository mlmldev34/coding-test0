def solution(s):
    arr=[str(i) for i in range(0,10)]
    if len(list(s))==4 or len(list(s))==6:
        return True if sum([1 if i in arr else 0 for i in list(s)])==len(list(s)) else False
    else:
        return False
    
        