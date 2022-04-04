def solution(n):
    num = str(bin(n)[2:])
    num = list('0'*(8-len(num)) + num)
    count = num.count('1')
    while n > 0:
        s = str(bin(n+1)[2:])
        s = list('0'*(8-len(s)) + s)
        c = s.count('1')
        if c == count:
            return int(''.join(s), 2)
            break
        n += 1
