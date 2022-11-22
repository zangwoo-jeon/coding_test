n = int(input())
array_f = list(map(int, input().split()))
array_s = list(map(int, input().split()))
array_f.sort()
array_s.sort(reverse=True)

result = 0
for i in range(n):
    result += array_f[i]*array_s[i]

print(result)
