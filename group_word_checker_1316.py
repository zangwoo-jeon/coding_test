n = int(input())

array = [list(map(str, input())) for _ in range(n)]

count = 0
for i in range(len(array)):
    count += 1
    result = [array[i][0]]
    for j in range(1, len(array[i])):
        if array[i][j-1] != array[i][j] and array[i][j] in result:
            count -= 1
            result = []
            break
        else:
            result.append(array[i][j])

print(count)
