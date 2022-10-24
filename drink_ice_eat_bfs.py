from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
result = 0
def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if graph[x][y] == 1:
        return False

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                Q.append((nx, ny))

    return True

for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            result += 1
print(result)