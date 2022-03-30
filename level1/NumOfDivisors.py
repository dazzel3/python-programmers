def solution(left, right):
    count = 0
    answer = []
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            answer.append(i)
        else:
            answer.append(-i)
        count = 0
    return sum(answer)
