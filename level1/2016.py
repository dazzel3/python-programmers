def solution(a, b):
    answer = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0
    for i in range(0, a-1):
        sum += day[i]

    sum += b
    return answer[sum % 7]
