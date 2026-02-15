"""
# 3273: 두 수의 합 
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

출력
문제의 조건을 만족하는 쌍의 개수를 출력한다.
"""

# 아래와 같이 이중 for 루프를 이용해 작성하면 시간 복잡도 O(n*n)으로 시간초과가 발생한다. 
n = int(input())
A = list(map(int, input().split())) # map 객체에 list 씌워주는 것 잊지 않기!!!
x = int(input())

def solution(n, A, x):
    ans = 0 # 조건을 만족하는 쌍의 수
    for i in range(n):
        for j in range(i+1, n):
            if A[i] + A[j] == x:
                ans += 1
    return ans

print(solution(n, A, x))



# 아래처럼 투 포인터 알고리즘으로 작성해야 한다.
"""
# Two Pointers:

- 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘
- 투포인터 알고리즘의 대표적인 문제: 어떤 숫자들의 리스트가 주어질 때, 해당 리스트의 연속 수열의 합이 특정 값을 가지는 것을 확인하는 문제
  - start, end 둘다 인덱스 0에서 시작하는 부분 연속 수열의 합이 있고,
  - start = index(0), right = len(A)-1에서 시작하는 pair-sum 투 포인터가 있음
"""

n = int(input())
A = list(map(int, input().split())) # map 객체에 list 씌워주는 것 잊지 않기!!!
x = int(input())

def solution(n, A, x):
    ans = 0 # 조건을 만족하는 쌍의 수
    interval_sum = 0 # 구간 합
    end = 0
    
    # start를 차례대로 증가시킴
    for start in range(n):
        # end만큼 증가시킴
        while interval_sum < x and end < n:
            interval_sum += A[end]
            end += 1 
        if interval_sum == x:
            ans += 1
        interval_sum -= A[start]
        
    return ans
        

# code ref: backjoon(3273) / 알고리즘 분류: 정렬, 투 포인터(두 포인터)