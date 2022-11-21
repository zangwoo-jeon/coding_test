n, m = map(int, input().split())
array = list(map(int, input().split()))

start = max(array)
end = sum(array)
result = sum(array)

while start <= end:
    count = 1
    length = 0
    mid = (start + end) // 2
    for i in range(n):
        if length + array[i] <= mid:
            length += array[i]
        else:
            length = array[i]
            count += 1

    if count <= m:
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1

print(result)
