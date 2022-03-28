def solution(dartResult):
    point = list(dartResult)
    answer = []
    now = 0
    for i in range(len(point)):
        if point[i] == '1' and point[i+1] == '0':
            now = 10
        elif point[i] == '0' and now == 10:
            if point[i-1] != '1':
                now = 0
            pass
        elif point[i] == 'S':
            answer.append(now ** 1)
        elif point[i] == 'D':
            answer.append(now ** 2)
        elif point[i] == 'T':
            answer.append(now ** 3)
        elif point[i] == '*':
            answer[len(answer)-1] *= 2
            if len(answer) > 1:
                answer[len(answer)-2] *= 2
        elif point[i] == '#':
            answer[len(answer)-1] *= (-1)
        else:
            now = int(point[i])
    return sum(answer)
