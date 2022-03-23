def solution(s):
    answer = ['zero', 'one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for i in range(0, len(answer)):
        if answer[i] in s:
            s = s.replace(answer[i], str(i))
    return int(s)
