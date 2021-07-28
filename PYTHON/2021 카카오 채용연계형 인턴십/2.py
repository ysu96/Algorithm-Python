from collections import deque
def solution(places):
    answer = []
    for place in places:
        graph = []
        persons = []
        for p in place:
            graph.append(list(p))

        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    persons.append((i,j))
        answer.append(check(graph,persons))

    return answer

def check(graph, persons):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for person in persons:
        x, y = person[0], person[1]
        q = deque([(x, y, 0)])
        visited = []
        while q:
            now_x, now_y, dist = q.popleft()
            if dist >= 2:
                continue
            visited.append((now_x,now_y))
            for i in range(4):
                nx = now_x + dx[i]
                ny = now_y + dy[i]
                if (nx,ny) in visited:
                    continue

                if 0 <= nx < 5 and 0 <= ny < 5:
                    if graph[nx][ny] == 'P':
                        return 0
                    if graph[nx][ny] == 'O':
                        q.append((nx,ny,dist+1))

    return 1

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
#[1, 0, 1, 1, 1]
print(solution(places))