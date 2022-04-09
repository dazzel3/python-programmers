def solution(people, limit):
    count = 0
    people.sort(reverse=True)
    i = 0
    j = len(people) - 1
    while i <= j:
        f = people[i]
        l = people[j]
        if f + l <= limit:
            j -= 1
        count += 1
        i += 1
    return count
