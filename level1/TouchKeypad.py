def solution(numbers, hand):
    loc = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1],
           6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}
    left = [3, 0]
    right = [3, 2]
    answer = ''
    for n in numbers:
        [x, y] = loc[n]
        if y == 0:
            answer += 'L'
            left = loc[n]
        elif y == 2:
            answer += 'R'
            right = loc[n]
        else:
            l = abs(left[0] - x) + abs(left[1] - y)
            r = abs(right[0] - x) + abs(right[1] - y)
            if l == r:
                if hand == 'right':
                    answer += 'R'
                    right = loc[n]
                elif hand == 'left':
                    answer += 'L'
                    left = loc[n]
            elif l > r:
                answer += 'R'
                right = loc[n]
            elif l < r:
                answer += 'L'
                left = loc[n]
    return answer
