
def dfs(tickets, route, is_visited, count, start):
    tlen = len(tickets)
    if count == tlen:
        return route

    for i in range(tlen):
        if is_visited[i] == False and tickets[i][0] == start:
            route.append(tickets[i][1])
            is_visited[i] = True
            new_route = dfs(tickets, route,is_visited, count+1, tickets[i][1])
            if new_route == None:
                is_visited[i] = False
                route.pop(-1)
            else: return new_route
    return None

def solution(tickets):
    route = ["ICN"]
    tlen = len(tickets)
    is_visited = [False for _ in range(tlen)]
    tickets.sort()
    count = 0
    answer = dfs(tickets, route, is_visited, count, "ICN")
    return answer



tickets = [["ICN", "SFO"], ["ICN", "SFO"], ["SFO", "ICN"], ["SFO", "ICN"], ["ICN","AAA"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))
# return = ["ICN", "JFK", "HND", "IAD"]

#["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]


# def dfs(tickets, here, is_visit, cnt):
#     n = len(tickets)
#     route = [here]
#
#     if n == cnt:
#         return (route, True)
#
#     for idx in range(n):
#         (a, b) = tickets[idx]
#         if (a == here) and (is_visit[idx] == False):
#             is_visit[idx] = True
#             (path, res) = dfs(tickets, b, is_visit, cnt+1)
#
#             if res == True:
#                 return (route + path, True)
#
#             is_visit[idx] = False
#
#     return (route, False)
#
# def solution(tickets):
#     start = tickets[0][0]
#     is_visit = [ False for _ in tickets ]
#     tickets = sorted(tickets)
#     (answer, res) = dfs(tickets, "ICN", is_visit, 0)
#     return answer if res else None