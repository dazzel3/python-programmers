def solution(id_list, report, k):
    r = list(set(report))
    answer = [0] * len(id_list)
    id_dic = {name: [] for name in id_list}
    for i in r:
        a, b = i.split()
        if a not in id_dic[b]:
            id_dic[b].append(a)
    for i in id_dic:
        if len(id_dic[i]) >= k:
            for j in id_dic[i]:
                answer[id_list.index(j)] += 1
    return answer
