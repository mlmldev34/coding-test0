def solution(price, money, count):
    result = money-sum([price*i for i in range(1,count+1)])
    return abs(result) if result<0 else 0