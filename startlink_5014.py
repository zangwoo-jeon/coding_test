from collections import deque

f, s, g, u, d = map(int, input().split())
dx = [u, -d]
graph = [0]*(f+1)
visit = [0]*(f+1)

def bfs(v):
    Q = deque()
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.popleft()
        if v == g:
            return graph[g]
        for i in range(2):
            nv = v + dx[i]
            if 1 <= nv <= f and visit[nv] == 0:
                visit[nv] = 1
                graph[nv] = graph[v] + 1
                Q.append(nv)
    if graph[g] == 0:
        graph[g] = "use the stairs"
        return graph[g]

print(bfs(s))