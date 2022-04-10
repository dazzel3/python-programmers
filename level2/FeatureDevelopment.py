def solution(progresses, s):
    answer = []
    p = [100-f for f in progresses]
    count = 0
    while len(p) > 0:
        for i in range(len(p)):
            p[i] -= s[i]
        while len(p) > 0:
            if p[0] <= 0:
                count += 1
                p.pop(0)
                s.pop(0)
            else:
                if count != 0:
                    answer.append(count)
                count = 0
                break
        if count != 0:
            answer.append(count)
    return answer
