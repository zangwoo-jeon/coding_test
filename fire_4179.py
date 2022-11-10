from collections import deque

r, c = map(int, input().split())

graph = [list(map(str, input())) for _ in range(r)]
JQ, FQ = deque(), deque()
J_visit, F_visit = [[0]*c for _ in range(r)], [[0]*c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while FQ:
        x, y = FQ.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != "#" and F_visit[nx][ny] == 0:
                    F_visit[nx][ny] = F_visit[x][y] + 1
                    FQ.append((nx, ny))

    while JQ:
        x, y = JQ.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == "." and J_visit[nx][ny] == 0:
                    if F_visit[nx][ny] == 0 or F_visit[nx][ny] > J_visit[x][y] + 1:
                        J_visit[nx][ny] = J_visit[x][y] + 1
                        JQ.append((nx, ny))
            else:
                return J_visit[x][y] + 1

    return "IMPOSSIBLE"

for i in range(r):
    for j in range(c):
        if graph[i][j] == "J":
            JQ.append((i, j))
        if graph[i][j] == "F":
            FQ.append((i, j))

print(bfs())