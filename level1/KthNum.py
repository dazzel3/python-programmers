def solution(array, commands):
    num = []
    answer = []
    for a in commands:
        i = a[0]
        j = a[1]
        k = a[2]
        num = sorted(array[i-1:j])
        answer.append(num[k-1])
    return answer
