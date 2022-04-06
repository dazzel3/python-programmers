def solution(s):
    l = s.split(' ')
    answer = ''
    for c in l:
        answer += c.capitalize()
        answer += ' '
    return answer[:-1]
