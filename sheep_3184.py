from collections import deque

r, c= map(int, input().split())

graph = [list(map(str, input())) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
sheep = 0
wolf = 0

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()
    Q.append((x, y))
    global sheep, wolf
    w_sheep, w_wolf = 0, 0
    visit[x][y] = 1
    if graph[x][y] == "o":
        w_sheep += 1
    if graph[x][y] == "v":
        w_wolf += 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "#" and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                Q.append((nx, ny))
                if graph[nx][ny] == "o":
                    w_sheep += 1
                if graph[nx][ny] == "v":
                    w_wolf += 1
    if w_sheep > w_wolf:
        w_wolf = 0
    else:
        w_sheep = 0
    sheep += w_sheep
    wolf += w_wolf


for i in range(r):
    for j in range(c):
        if graph[i][j] != "#" and visit[i][j] == 0:
           bfs(i, j)

print(sheep, wolf)
