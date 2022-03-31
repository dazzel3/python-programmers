def solution(seoul):
    x = 0
    for i in seoul:
        if (i == "Kim"):
            x = seoul.index(i)
    return "김서방은 " + str(x) + "에 있다"
