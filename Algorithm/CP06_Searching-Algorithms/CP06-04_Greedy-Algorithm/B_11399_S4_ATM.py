# 11399: ATM

n = int(input())
p = list(map(int, input().split()))

p.sort()

prefix_sum = 0
answer = 0

for time in p:
    prefix_sum += time
    answer += prefix_sum 

print(answer)


# code ref: backjoon(11399) / 알고리즘 분류: 그리디 알고리즘, 정렬 