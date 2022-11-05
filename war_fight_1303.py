from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(m)]
visit = [[0]*n for _ in range(m)]
I = 0
Y = 0

def bfs(x, y):
    global I, Y
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()
    Q.append((x, y))
    sol = 1
    visit[x][y] = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                sol += 1
                visit[nx][ny] = 1
                Q.append((nx, ny))
    return sol


for i in range(m):
    for j in range(n):
        if visit[i][j] == 0 and graph[i][j] == "W":
            I += bfs(i,j)**2
        if visit[i][j] == 0 and graph[i][j] == "B":
            Y += bfs(i,j)**2

print(I, Y)