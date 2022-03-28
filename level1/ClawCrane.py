def solution(board, moves):
    answer = [0]
    result = 0

    for i in moves:
        for j in range(len(board[0])):
            target = board[j][i-1]
            if target != 0:
                if answer[len(answer)-1] == target:
                    answer.pop(len(answer)-1)
                    result += 2
                else:
                    answer.append(target)
                board[j][i-1] = 0
                break
    return result
