n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    result = 0
    for i in range(sx-1, ex):
        for j in range(sy-1, ey):
            result += graph[i][j]
    print(result)
