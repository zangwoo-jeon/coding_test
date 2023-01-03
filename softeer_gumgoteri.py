w, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

array.sort(key=lambda x:-x[1])

result = 0
for i in range(n):
    if w > array[i][0]:
        result += array[i][0] * array[i][1]
        w -= array[i][0]
    else:
        result += w * array[i][1]
        break

print(result)
