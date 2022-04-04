def solution(n):
    answer = ''
    num = ['4', '1', '2']
    while n > 0:
        r = n % 3
        answer = num[r] + answer
        n = (n-1)//3
    return answer
