def solution(s):
    s = list(s)
    left = 0
    right = 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
            if left == 0:
                return False
            elif left == right:
                left = 0
                right = 0
    if left > right:
        return False
    return True
