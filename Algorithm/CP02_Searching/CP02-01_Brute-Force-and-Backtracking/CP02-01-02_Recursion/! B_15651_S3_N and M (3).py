# 15651: N과 M (3)


# 1) 문제 조건 그대로 재귀/ 백트래킹으로 풀기
N, M = map(int, input().split())

seq = []

def backtrack(depth):
    if depth == M:
        print(*seq)
        return 
    
    for i in range(N):
        seq.append(i+1)

        backtrack(depth+1)
        
        seq.pop()

backtrack(0)


# 2) 파이썬 내장 함수 사용
N, M = map(int, input().split())


from itertools import product 

num_li = product(range(1, N+1), repeat = M)
for num in num_li:
    print(*num)


# code ref: backjoon(15651) / 알고리즘 분류: 백트래킹
