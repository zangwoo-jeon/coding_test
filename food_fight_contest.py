Food = list(map(int, input().split()))

def solution(food):
    answer = ""
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            answer += str(i)
    answer += str(0)
    for i in range(len(food)-1, 0, -1):
        for j in range(food[i]//2):
            answer += str(i)
    return answer

print(solution(Food))

def S(food):
    answer = ""
    rev = ""
    for i in range(1, len(food)):
        answer += str(i)*(food[i]//2)
    rev = answer[::-1]
    answer += "0"

    return answer + rev

print(S(Food))