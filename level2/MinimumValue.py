def solution(a, b):
    a.sort()
    b.sort(reverse=True)
    total = 0
    for i in a:
        num = b[0]
        total += i * num
        b.remove(num)
    return total
