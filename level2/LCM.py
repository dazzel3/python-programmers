def solution(arr):
    n = max(arr)
    x = 1
    count = 0
    while True:
        for i in arr:
            if n % i == 0:
                count += 1
        if count == len(arr):
            return n
        x += 1
        n = max(arr)
        n = n * x
        count = 0
