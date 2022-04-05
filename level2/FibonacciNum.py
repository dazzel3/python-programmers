def solution(n):
    answer = [0, 1]
    num = 0
    for i in range(n-1):
        num = answer[i] + answer[i+1]
        answer.append(num)
    return answer[len(answer)-1] % 1234567
