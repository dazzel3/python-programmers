def solution(p, loc):
    result = 0
    while len(p):
        n = max(p)
        first = p.pop(0)
        if n == first:
            result += 1
            if loc == 0:
                return result
        else:
            p.append(first)
        loc -= 1
        if loc < 0:
            loc = len(p)-1
