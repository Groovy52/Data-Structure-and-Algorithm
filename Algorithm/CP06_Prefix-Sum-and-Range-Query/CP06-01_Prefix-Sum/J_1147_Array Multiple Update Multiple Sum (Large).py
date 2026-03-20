# 11147: 배열 다중 업데이트 다중 합 (Large)

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list()
for _ in range(m):
    B.append(list(map(int, input().split())))

P = [0]*n 

flag = False

for b in B:
    if b[0]==1:
        P[b[1]] += b[3]
        if b[2] <= n-2:
            P[b[2] + 1] -= b[3]
    
    if b[0]==2:
        if flag == False:
            for idx in range(1, n):
                P[idx] += P[idx-1]
                flag = True
        """
        이렇게 작성하면
        유형 2가 마지막에 1번만 등장하냐, 여러번 등장 가능하냐에 따라 시간복잡도가 달라지고
        아래처럼 작성했는데, 여러번 등장할 경우 시간 복잡도가 O(n x m)으로 너무 커질 수 있다.
        """
        print(sum(P[b[1]: b[2]+1]) + sum(A[b[1]: b[2]+1]))

# 고친 코드
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list()
for _ in range(m):
    B.append(list(map(int, input().split())))

"""
다음 조건을 이용해야 함.
=> 배열 B에는 모든 유형 1의 질의가 유형 2의 질의보다 앞부분에 저장되어 있다.

"""
P = [0]*n 
flag = False
for b in B:
    if b[0] == 1:
        P[b[1]] += b[3]
        if b[2] <= n-2:
            P[b[2] + 1] -= b[3]
    else:
        if flag == False:
            flag = True
            for i in range(1, n):
                P[i] += P[i - 1]

            for i in range(n):
                A[i] += P[i]

            P2 = [0] * n # 누적합에 대한 누적합을 적용하면 유형 2에서 sum을 써서 시간초과 발생하는 것을 방지할 수 있음
            P2[0] = A[0]
            for i in range(1, n):
                P2[i] = P2[i-1] + A[i]

        if b[1] == 0:
            print(P2[b[2]])
        else:
            print(P2[b[2]] - P2[b[1]-1])


# code ref: joonlab(1147) / 알고리즘 분류: 누적합