T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    graph = [[0]*(n+1) for _ in range(k+1)]

    for i in range(n+1):
        graph[0][i] = i

    for i in range(k+1):
        graph[i][1] = 1

    for i in range(1, k+1):
        for j in range(2, n+1):
            graph[i][j] += graph[i-1][j] + graph[i][j-1]

    print(graph[k][n])
