from collections import deque

n, m, k = map(int, input().split())

graph = [[0]*m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

def bfs(x, y):
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                Q.append((nx, ny))
                result += 1
    return result

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer = max(answer, bfs(i, j))

print(answer)