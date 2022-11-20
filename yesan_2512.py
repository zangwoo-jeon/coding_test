n = int(input())
array = list(map(int, input().split()))
m = int(input())

result = 0
start = 1
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += mid
        else:
            total += i
    if total > m:
        end = mid - 1
    else:
        result = mid
        start = mid+1
print(result)