def solution(n, lost, reserve):
    pos = n - len(lost)

    res = [i for i in reserve if i not in lost]
    los = [i for i in lost if i not in reserve]
    pos = pos + (len(reserve) - len(res))

    res.sort()
    los.sort()

    count = 0
    for i in res:
        if i == 1 and (i+1 in los):
            los.remove(i+1)
            count += 1
        elif i-1 in los:
            los.remove(i-1)
            count += 1
        elif i+1 in los:
            los.remove(i+1)
            count += 1
    return pos + count
