from collections import deque

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    result = 0
    Q = deque()
    Q.append((x, y))
    visit = [[0] * m for _ in range(n)]
    visit[x][y] = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and graph[nx][ny] == "L":
                Q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
                result = visit[nx][ny]
    return result -1

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":

            count = max(count, bfs(i, j))

print(count)
