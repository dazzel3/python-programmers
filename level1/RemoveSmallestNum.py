def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
        return answer
    else:
        num = min(arr)
        arr.remove(num)
        return arr
