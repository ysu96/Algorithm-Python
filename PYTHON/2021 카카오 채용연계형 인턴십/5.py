from itertools import combinations
import copy
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def solution(k, num, links):
    answer = 1e9
    n = len(num)
    graph = [[] for _ in range(n)]
    edges = []
    for i,link in enumerate(links):
        for l in link:
            if l == -1:
                continue
            else:
                graph[i].append(l)
                graph[l].append(i)
                edges.append((i,l))

    if k == 1:
        return sum(num)
    # elif k==2:
    #     candidates = edges
    else:
        candidates = list(combinations(edges,k-1))
    # print(candidates)


    for candidate in candidates:
        parent = [i for i in range(n)]
        test_graph = copy.deepcopy(graph)
        test_edge = copy.deepcopy(edges)
        for a,b in candidate:
            test_graph[a].remove(b)
            test_graph[b].remove(a)
            if (a,b) in test_edge:
                test_edge.remove((a,b))
            else:
                test_edge.remove((b,a))
        # print(test_edge)
        for _ in range(2):
            for e in test_edge:
                a, b = e
                if find_parent(parent, a) != find_parent(parent, b):
                    union_parent(parent, a, b)

        # print(parent)
        parent_dict = dict()
        for i in range(n):
            parent_dict[parent[i]] = 0
        for i in range(n):
            parent_dict[parent[i]] += num[i]


        # print(parent_dict)
        max_sum = max(parent_dict.values())
        # print(max_sum)
        answer = min(answer,max_sum)


    return answer


# 3	[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]	[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]	40
# 1	[6, 9, 7, 5]	[[-1, -1], [-1, -1], [-1, 0], [2, 1]]	27
k=2
num=[6, 9, 7, 5]
links=[[-1, -1], [-1, -1], [-1, 0], [2, 1]]
#14
print(solution(k,num,links))
# 4	[6, 9, 7, 5]	[[-1, -1], [-1, -1], [-1, 0], [2, 1]]