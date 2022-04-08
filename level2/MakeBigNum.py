def solution(number, k):
    n = list(number)
    count = 0
    answer = []
    for i in range(len(n)):
        while k > 0 and len(answer) > 0 and answer[len(answer)-1] < n[i]:
            answer.pop()
            k -= 1
        answer.append(n[i])
    return "".join(answer[:len(answer)-k])
