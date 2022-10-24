from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
result = 0

def bfs(x, y):
    global result
    graph[x][y] = 0
    Q = deque()
    Q.append((x, y))
    result += 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                Q.append((nx, ny))
                result += 1
    return result

count = 0
answer = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))
            result = 0
            count += 1

print(count)
answer.sort()
for i in answer:
    print(i)