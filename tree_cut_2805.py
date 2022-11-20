n, m = map(int, input().split())

array = list(map(int, input().split()))

result = 0

start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in array:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid-1

    else:
        result = mid
        start = mid+1
print(result)