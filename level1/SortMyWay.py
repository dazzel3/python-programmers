def solution(strings, n):
    answer = sorted(strings)
    print(answer)
    for i in range(1, len(strings)):
        for j in range(1, len(strings)):
            if answer[j][n] < answer[j-1][n]:
                answer[j-1], answer[j] = answer[j], answer[j-1]
    return answer
