from collections import deque

r, c = map(int, input().split())

graph = [list(map(str, input())) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[0] * c for _ in range(r)]
Q = deque()

def bfs(Dx, Dy):
    while Q:
        x, y = Q.popleft()
        if graph[Dx][Dy] == "S":
            return visit[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (graph[nx][ny] == "." or graph[nx][ny] == "D") and graph[x][y] == "S":
                    graph[nx][ny] = "S"
                    visit[nx][ny] = visit[x][y] + 1
                    Q.append((nx, ny))

                if (graph[nx][ny] == "." or graph[nx][ny] == "S") and graph[x][y] == "*":
                    graph[nx][ny] = "*"
                    Q.append((nx, ny))

    return "KAKTUS"

for i in range(r):
    for j in range(c):
        if graph[i][j] == "S":
            Q.append((i, j))
        if graph[i][j] == "D":
            Dx, Dy = i, j

for i in range(r):
    for j in range(c):
        if graph[i][j] == "*":
            Q.append((i, j))

print(bfs(Dx, Dy))