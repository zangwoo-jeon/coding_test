while True:
    graph = list(map(int, input().split()))
    count = 0

    if graph[0] == -1:
        break

    for i in range(len(graph)-1):
        for j in graph:
            if graph[i]*2 == j:
                count += 1

    print(count)