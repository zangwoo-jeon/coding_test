from collections import deque
T = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs(x, y, a, b):
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        x, y = Q.popleft()
        if x == a and y == b:
            return visit[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                Q.append((nx, ny))

for _ in range(T):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    print(bfs(start_x, start_y, end_x, end_y))
