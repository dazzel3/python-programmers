def solution(N, stages):
    answer = {stage: 0 for stage in range(1, N+1)}
    stages.sort()
    l = len(stages)
    n = 0
    for i in range(1, N+1):
        n = stages.count(i)
        if n == 0:
            fail = 0
        else:
            fail = n / l
        l -= n
        answer[i] = fail

    a = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    result = []
    for key, vaule in a:
        result.append(key)
    return result
