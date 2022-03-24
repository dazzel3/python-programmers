def solution(new_id):
    ch = ['-', '_', '.']
    for i in range(ord('a'), ord('z')+1):
        ch.append(chr(i))
    for i in range(0, 10):
        ch.append(str(i))

    answer = ''
    answer = new_id.lower()
    for i in answer:
        if i not in ch:
            answer = answer.replace(i, '')
    answer = answer.split('.')

    removed = ''
    answer = [i for i in answer if i != removed]

    result = ''
    if len(answer) == 0:
        result = 'a'
    else:
        result = '.'.join(answer)

    if len(result) > 15:
        result = result[:15]
        if result[-1:] == '.':
            result = result[:14]
    if len(result) < 3:
        while (len(result) != 3):
            result += result[-1:]
    return result
