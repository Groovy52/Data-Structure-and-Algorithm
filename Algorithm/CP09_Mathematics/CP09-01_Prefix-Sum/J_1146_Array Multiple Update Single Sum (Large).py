# 1146: 배열 다중 업데이트 다중 합(Large)

# 에러 코드
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = []
for _ in range(m):
    B.append(list(map(int, input().split())))

P = [0]*n

for b in B:
    if b[0]==1:
        P[b[1]] += b[3]
        P[b[2] + 1] -= b[3] # => 0 ≤ i ≤ j ≤ n - 1 라는 문제 조건을 잘 확인해야 함. 
    else:
        for idx in range(1, n):
            P[idx] += P[idx-1]
        for idx in range(n):
            A[idx] += P[idx]
        print(sum(A[b[1]: b[2]+1]))

# 에러 고친 코드
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = []
for _ in range(m):
    B.append(list(map(int, input().split())))

P = [0]*n

for b in B:
    if b[0]==1:
        P[b[1]] += b[3]
        if b[2] <= n-2: # ??? P[b[2]+1]은 존재하지 않는 인덱스에 직접 접근하므로 범위를 넘으면 에러가 날 수 있어 검사해야 하고, 
            P[b[2] + 1] -= b[3] 
    else:
        for idx in range(1, n):
            P[idx] += P[idx-1]
        for idx in range(n):
            A[idx] += P[idx]
        print(sum(A[b[1]: b[2]+1])) # ??? A[b[1]:b[2]+1]은 슬라이싱이라서 끝 인덱스가 배열 길이와 같아도 괜찮음, 넘어도 됨.

# code ref: joonlab(1146) / 알고리즘 분류: 누적합