from collections import deque
T = int(input())

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()
    Q.append((x, y))
    graph[x][y] = "."
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == "#":
                graph[nx][ny] = "."
                Q.append((nx, ny))

    return True

for _ in range(T):
    H, W = map(int, input().split())
    graph = [list(map(str, input())) for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == "#":
                bfs(i, j)
                count += 1
    print(count)