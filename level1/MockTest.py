def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []

    def num(p):
        count = 0
        n = p * (len(answers) // len(p))
        for i in range(len(answers) % len(p)):
            n.append(p[i])
        for i in range(len(answers)):
            if answers[i] == n[i]:
                count += 1
        return count
    if num(p1) == num(p2) == num(p3):
        answer = [1, 2, 3]
        return answer
    else:
        if num(p1) == max(num(p1), num(p2), num(p3)):
            answer.append(1)
        if num(p2) == max(num(p1), num(p2), num(p3)):
            answer.append(2)
        if num(p3) == max(num(p1), num(p2), num(p3)):
            answer.append(3)
        return sorted(answer)
