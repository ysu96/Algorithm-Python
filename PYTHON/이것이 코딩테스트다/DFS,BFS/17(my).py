n,k = map(int,input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

data_n = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        data_n[i][j] = data[i][j]

s,x,y = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spread(x,y):
    temp = data[x][y]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and nx<n and ny>=0 and ny<n and data_n[nx][ny] == 0:
            data_n[nx][ny] = temp

def virus():
    for v in range(1,k+1):
        for i in range(n):
            for j in range(n):
                if data[i][j] == k:
                    spread(i,j)

    for i in range(n):
        for j in range(n):
            data[i][j] = data_n[i][j]

for i in range(s):
    virus()

if data[x-1][y-1] != 0:
    print(data[x-1][y-1])
else:
    print(0)
