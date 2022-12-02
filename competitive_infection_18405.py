from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

Q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 종류대로 Q에 넣기
for a in range(1, k+1):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == a:
                Q.append((i, j))

def bfs():
    time = 0
    while Q:
        if time == s:
            return
        # 현재 바이러스들이 한 번 씩 전염한 다음에 시간 1 증가 
        for _ in range(len(Q)):
            x, y = Q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    Q.append((nx, ny))
        time += 1

bfs()

print(graph[x-1][y-1])
