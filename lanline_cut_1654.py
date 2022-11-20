n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

result = 0
start = 1
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        total += i // mid

    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)