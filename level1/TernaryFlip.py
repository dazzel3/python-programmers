def solution(n):
    answer = []
    while n // 3 != 0:
        answer.append(str(n % 3))
        n = n // 3
    answer.append(str(n % 3))
    return int(''.join(answer), 3)
