from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

maximum = 0

for i in graph:
    for j in i:
        maximum = max(maximum, j)

def bfs(x, y, rain):
    Q = deque()
    Q.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > rain and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                Q.append((nx, ny))

result = 0
for k in range(maximum):
    visit = [[0]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visit[i][j] == 0:
                bfs(i, j, k)
                count += 1
    result = max(result, count)

print(result)