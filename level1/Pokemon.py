def solution(nums):
    select = len(nums)//2
    a = list(set(nums))
    if select == len(a):
        return select
    elif select < len(a):
        return select
    elif select > len(a):
        return len(a)
