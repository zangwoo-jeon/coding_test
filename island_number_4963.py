from collections import deque

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    while Q:
        x, y = Q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                Q.append((nx, ny))


answer = []

while True:
    w, h = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(h)]

    result = 0
    if w == 0 and h == 0:
        break

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1
    answer.append(result)

for i in answer:
    print(i)
    
'''
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                Q.append((nx, ny))
    return True

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and bfs(i, j) == True:
                result += 1
    print(result)
'''
