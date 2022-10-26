import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)

answer = []

while True:
    result = 0
    w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]

    if w == 0 and h == 0:
        break

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1
    answer.append(result)

for i in answer:
    print(i)