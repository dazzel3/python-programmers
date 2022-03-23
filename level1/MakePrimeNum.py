import itertools


def solution(nums):
    count = 0
    result = 0
    it = itertools.combinations(nums, 3)
    for i in it:
        for j in range(1, sum(i)+1):
            if sum(i) % j == 0:
                count += 1
        if count == 2:
            result += 1
        count = 0
    return result
