def solution(phone_number):
    a = list(phone_number)
    for i in range(len(a)):
        if i not in range(len(a)-4, len(a)):
            a[i] = '*'
    return ''.join(a)
