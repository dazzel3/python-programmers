def solution(n):
    s = list(str(n))
    total = 0
    for i in s:
        total = total + int(i)
    return total
