def solution(lottos, win_nums):
    zero = lottos.count(0)
    num = len([i for i in lottos if i in win_nums])
    answer = [num, num+zero]
    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = 6
        elif answer[i] == 1:
            answer[i] = 6
        elif answer[i] == 2:
            answer[i] = 5
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 6:
            answer[i] = 1
    return sorted(answer)
