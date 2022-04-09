def solution(skill, skill_trees):
    count = 0
    for i in skill_trees:
        s = list(skill)
        n = True
        for j in i:
            if j in skill:
                if j == s[0]:
                    s.pop(0)
                else:
                    n = False
                    break
        if n == True:
            count += 1
    return count
