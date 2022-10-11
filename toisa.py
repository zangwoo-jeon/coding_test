N = int(input())
#t : 날짜, p : 금액, answer : 정답 리스트
t = [0]*16
p = [0]*16
answer = [0]*16

for i in range(N):
    A, B = map(int, input().split())
    t[i] = A
    p[i] = B
    # 걸리는 날짜가 N보다 크면 값 0
    if i + t[i] > N:
        t[i] = 0
        p[i] = 0

# 정답은 다음날의 값 vs 현재 받을 값과 현재 임무를 수행 했을 때와 한 뒤에 받을 돈 중 큰 값
for i in range(N-1, -1, -1):
    answer[i] = max(answer[i+1], answer[i + t[i]] + p[i])

print(answer[0])