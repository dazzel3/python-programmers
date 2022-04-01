def solution(s):
    count_p = 0
    count_y = 0
    for i in s:
        if i == 'p' or i == 'P':
            count_p += 1
        if i == 'y' or i == 'Y':
            count_y += 1
    if count_p == count_y:
        return True
    else:
        return False
