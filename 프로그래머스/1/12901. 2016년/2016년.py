def solution(a, b):
    d=4
    arr=[31,29,31,30,31,30,31,31,30,31,30,31]
    brr=['SUN','MON','TUE','WED','THU','FRI','SAT']
    return brr[(d+b+sum(arr[:(a-1)]))%7]