def solution(n):
    s = n**(1/2)
    if (s % 1) == 0:
        return (int(s)+1)**2
    else:
        return -1
