def solution(arr, divisor):
    answer = []
    count = 0
    for i in arr:
        if (i % divisor) == 0:
            answer.append(i)
            count = count + 1
    if count == 0:
        answer.append(-1)
        return answer
    else:
        answer.sort()
        return answer
