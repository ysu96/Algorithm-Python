from collections import deque
n,l,r = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = []
def check(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if abs(A[nx][ny]-A[x][y]) >= l and abs(A[nx][ny]-A[x][y]) <= r:
                if (nx,ny) not in q:
                    if (x,y) not in q:
                        q.append((x,y))
                    q.append((nx,ny))

def solution():
    count = 0
    union = []

    while 1:
        for i in range(n):
            for j in range(n):
                check(i,j)
                q.sort()
        #print(q)
        if len(q) == 0:
            return count

        while q:

            if len(union) == 0:
                nx, ny = q[0]
                union.append((nx,ny))

            #연합인지 확인
            for x,y in union:
                for i in q:
                    #큐에서 인접하면
                    if (abs(i[0]-x) == 1 and i[1]==y) or (abs(i[1]-y)==1 and i[0]==x):
                        if abs(A[i[0]][i[1]] - A[x][y]) >= l and abs(A[i[0]][i[1]] - A[x][y]) <= r:
                            if i not in union:
                                union.append(i)

            for i in union:
                q.remove(i)

            #print(union)
            sum = 0
            for x,y in union:
                sum += A[x][y]
            sum = sum // len(union)
            for x,y in union:
                A[x][y] = sum
            #print(A, count)
            union = []
        count += 1

print(solution())




