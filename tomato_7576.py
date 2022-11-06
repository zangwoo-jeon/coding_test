from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
to = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            to.append((i, j))
count = 0
def bfs():
    Q = deque(to)
    global count
    while Q:
        for _ in range(len(Q)):
            x, y = Q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    Q.append((nx, ny))

        count += 1
    return count
bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
print(count-1)
