from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0]*m for _ in range(n)]

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                Q.append((nx, ny))

for i in range(m):
    if graph[0][i] == 0:
        bfs(0, i)

print("YES" if 1 in visit[-1] else "NO")
