def solution(record):
    answer = {}
    result = []
    b = ['님이 들어왔습니다.', '님이 나갔습니다.']
    for r in record:
        r = r.split(" ")
        if r[0] == 'Enter' or r[0] == 'Change':
            if r[1] in answer:
                answer[r[1]] = r[2]
            answer[r[1]] = r[2]

    for r in record:
        r = r.split(" ")
        if r[0] == 'Enter':
            result.append(answer[r[1]]+b[0])
        elif r[0] == 'Leave':
            result.append(answer[r[1]]+b[1])
    return result
