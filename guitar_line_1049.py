n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(m)]
B_array = sorted(array, key=lambda x:(x[1], x[0]))
A_array = sorted(array, key=lambda x:(x[0], x[1]))
result = 0

if A_array[0][0] < 6 * B_array[0][1]:
    result += A_array[0][0] * (n // 6) + min(A_array[0][0], B_array[0][1]*(n%6))

else:
    result += B_array[0][1] * n

print(result)
