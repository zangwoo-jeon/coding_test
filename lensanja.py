n = int(input())
# 값
graph = list(map(int, input().split()))
# 연산자 수 + - * /
yeonsan = list(map(int, input().split()))

maximum_number = -(10**10)
minimum_number = (10**10)

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum_number, minimum_number
    if depth == n:
        maximum_number = max(total, maximum_number)
        minimum_number = min(total, minimum_number)
        return

    if plus:
        dfs(depth+1, total + graph[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - graph[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth+1, total * graph[depth], plus, minus, multiply - 1, divide)
    if divide:
        # int(a / b) 하면 음수여도 양수로 계산한뒤 음수 변환
        dfs(depth + 1, int(total / graph[depth]), plus, minus, multiply, divide - 1)

dfs(1, graph[0], yeonsan[0], yeonsan[1], yeonsan[2], yeonsan[3])
print(maximum_number)
print(minimum_number)