# 11047: 동전 0

N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

A.sort(reverse=True)

count = 0

for coin in A:
    count += K // coin 
    K %= coin 

print(count)

# code ref: backjoon(11047) / 알고리즘 분류: 그리디 알고리즘 