"""

# 1092: 식당 입구 대기 줄

여러 명의 학생이 식사하기 위하여 학교 식당을 향해 달려가고 있다. 학교 식당에 도착한 학생은 식당 입구에 줄을 서서 대기한다. 
학교 식당에 먼저 도착한 학생이 나중에 도착한 학생보다 식당 입구의 앞쪽에서 대기한다. 
식사는 1인분씩 준비된다. 식사 1인분이 준비되면 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식당으로 들어가서 식사를 시작한다. 
식사를 시작한 학생은 항상 식사를 마친다.

학생이 학교 식당에 도착하고 식사가 준비되는 n개의 정보가 저장된 A가 주어진다. 
A에 저장된 첫 번째 정보부터 n번째 정보까지 순서대로 처리한 다음, 식당 입구에 줄을 서서 대기하는 학생 수가 최대가 
되었던 순간의 학생 수와 이때 식당 입구의 맨 뒤에 대기 중인 학생의 번호를 출력하자. 대기하는 학생 수가 최대인 경우가 
여러 번이라면 맨 뒤에 줄 서 있는 학생의 번호가 가장 작은 경우를 출력하자.

A에 저장된 n개의 정보는 아래 두 가지 유형으로 구분된다. 첫 번째가 유형 1, 
두 번째가 유형 2이다.

- 1 a : 학생 번호가 양의 정수 a인 학생 1명이 학교 식당에 도착하여 식당 입구의 맨 뒤에 줄을 서기 시작한다.
- 2   : 식사 1인분이 준비되어 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식사를 시작한다.

식사 1인분이 준비될 때는 식당 입구에서 대기 중인 학생이 항상 존재한다. 식당 입구에 줄을 서서 대기하였으나 
식사가 준비 안 된 학생은 식사를 못 한다.

"""

# 1) 학생수가 최대일 때 최대 num 갱신, 최대 num이 같을 때에는 대기 뒷 번호가 작을 때 갱신 => 문제 그대로 조건식으로 표현
import sys

input = sys.stdin.readline
n = int(input())
A = list(list(map(int, input().split())) for _ in range(n))

def solution(n, A):
    from collections import deque 
    q = deque()

    max_len = 0
    min_num = 0
    for info in A:
        if info[0] == 1:
            q.append(info[1])
            
            if max_len < len(q) or (max_len == len(q) and info[1] < min_num): 
                max_len = len(q)
                min_num = info[1]
            
            # if max_len < len(q):
            #     max_len = len(q)
            #     min_num = info[1]
            # elif max_len == len(q) and info[1] < min_num:
            #     min_num = info[1]
        
        else:
            q.popleft()
    
    return [max_len, min_num]

S = solution(n, A)
print(S[0], S[1])    


# 1-2) 더 짧은 코드
def solution(n, A):
    from collections import deque 
    q = deque()
    
    ans = [0, 0]
    for info in A:
        if info[0] == 1:
            q.append(info[1])
            
            if ans[0] < len(q):
                ans = [len(q), info[1]]
            elif ans[0] == len(q):
                ans[1] = min(info[1], ans[1])
        else:
            q.popleft()
    return ans

print(*solution(n, A)) # * = “컨테이너를 풀어서(unpack) 안에 있는 값들을 개별 인자로 전달”하는 연산자. 

# 2) 문제 조건은 나중에 반환 시 적용
import sys

input = sys.stdin.readline
n = int(input())
A = list(list(map(int, input().split())) for _ in range(n))

def solution(n, A):
    from collections import deque 
    q = deque()

    w = [] # 대기 줄 정보, append (대기 중인 학생 수, 대기될 때 학생 번호)
    for info in A:
        if info[0] == 1:
            q.append(info[1])
            q_num = info[1]
        else:
            q.popleft()
        q_len = len(q)
        w.append((q_len, q_num))

    return sorted(w, key = lambda x: (-x[0], x[1]))[0]

S = solution(n, A)
print(S[0], S[1])     

 

# code reference: joonlab(1092) / 백준 26042 (실버 5) / 알고리즘 분류: 구현, 자료 구조, 큐