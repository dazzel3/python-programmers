def solution(x):
    text = str(x)
    total = 0
    for i in text:
        total = total + int(i)
    if (x % total) == 0:
        return True
    else:
        return False
