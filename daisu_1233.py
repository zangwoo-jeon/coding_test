a,b,c = map(int, input().split())

dp = [0]*(a+b+c+1)

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            dp[i+j+k] += 1

for i in range(len(dp)):
    if dp[i] == max(dp):
        print(i)
        break