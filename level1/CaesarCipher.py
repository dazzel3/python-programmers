def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) in range(ord('a'), ord('z')+1):
            if ord(i)+n > ord('z'):
                num = ord(i)+n-26
            else:
                num = ord(i)+n
            answer = answer + chr(num)
        elif ord(i) in range(ord('A'), ord('Z')+1):
            if ord(i)+n > ord('Z'):
                num = ord(i)+n-26
            else:
                num = ord(i)+n
            answer = answer + chr(num)
        else:
            answer = answer + i
    return answer
