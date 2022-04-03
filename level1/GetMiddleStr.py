def solution(s):
    num = len(s)
    div = num // 2
    if num % 2 == 0:
        return s[div-1:div+1]
    else:
        return s[div:div+1]
