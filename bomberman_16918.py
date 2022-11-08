from collections import deque

r, c, n = map(int, input().split())

Graph = []
bomb = []
for i in range(r):
    Graph.append(list(map(str, input())))
    for j in range(c):
        if Graph[i][j] == "O":
            bomb.append((i, j))


def bfs(graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque(bomb)
    result = 1
    if n % 2 == 0:
        All_bomb = [["O"] * c for _ in range(r)]
        return All_bomb
    while Q:
        if n % 2 == 0:
            All_bomb = [["O"] * c for _ in range(r)]
            return All_bomb
        if result == n:
            break
        graph = [["O"] * c for _ in range(r)]
        result += 2
        for _ in range(len(Q)):
            x, y = Q.popleft()
            graph[x][y] = "."
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    graph[nx][ny] = "."
        for i in range(r):
            for j in range(c):
                if graph[i][j] == "O":
                    Q.append((i, j))

    return graph

for i in bfs(Graph):
    print("".join(i))