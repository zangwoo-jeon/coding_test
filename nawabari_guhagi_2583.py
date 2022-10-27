from collections import deque

m, n, k = map(int, input().split())

graph = [[0]*n for _ in range(m)]


for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(m-d, m-b):
        for j in range(a, c):
            graph[i][j] = 1


def bfs(x, y):
    result = 1
    Q = deque()
    Q.append((x, y))
    graph[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                Q.append((nx, ny))
                result += 1
    return result


count = 0
answer = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            answer.append(bfs(i, j))
            count += 1
print(count)
answer.sort()
print(*answer)