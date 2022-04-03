def solution(n):
    s = list(str(n))
    s.reverse()
    answer = []
    for i in s:
        answer.append(int(i))
    return answer
