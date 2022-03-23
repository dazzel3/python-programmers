def solution(d, budget):
    d.sort()
    result = 0
    for i in range(len(d)):
        if budget - d[i] >= 0:
            budget -= d[i]
            result += 1
    return result
