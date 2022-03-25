def solution(sizes):
    s = []
    l = []
    for i in sizes:
        i.sort()
        for j in range(len(i)):
            if j == 0:
                s.append(i[j])
            else:
                l.append(i[j])
    return max(s) * max(l)
