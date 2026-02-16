"""
1608: 값이 k인 트리 노드의 깊이

문제 설명
n개의 정점과 n - 1개의 간선으로 구성된 트리 T가 있다. 정점 번호는 0부터 n - 1까지이고 0번 정점이 루트이다. 
간선에는 가중치가 없다. 트리 T에 있는 각 정점에는 서로 다른 값이 부여된다. 트리 T에서 정점에 부여된 값이 k인 
노드의 깊이(depth)를 출력하자. 루트 정점의 깊이는 0이고 자식 정점의 깊이는 부모 정점의 깊이보다 1만큼 더 큰 값을 갖는다. 
참고로, 파이썬 언어로 제출할 때는 제한 사항에 있는 setrecursionlimit() 함수를 사용하자.
"""

# 1)
import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
edges = list(list(map(int, input().split())) for _ in range(n-1))
A = list(map(int, input().split()))

def solution(n, k, edges, A):
    E = [[] for _ in range(n)]
    for p, c in edges:
        E[p].append(c)
    
    return solve(0, 0, E, A, k)
    
def solve(curr_n, curr_d, E, A, k):
    if A[curr_n] == k:
        return curr_d
    
    for v in E[curr_n]:
        ret = solve(v, curr_d + 1, E, A, k)
        if ret != -1:
            return ret
    
    return -1

print(solution(n, k, edges, A))


# 2)
import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    p, c = map(int, input().split())
    tree[p].append(c)
values = list(map(int, input().split()))

def solution(tree, values, k):
    global answer
    
    # 현재 노드 = 루트 노드에서 출발, 깊이 = 0에서 출발 
    dfs(0, 0, tree, values, k)
    return answer 
    
def dfs(node, depth, tree, values, k):
    global answer 
    
    # 현재 노드의 값이 k라면 answer=depth 로 업데이트 
    if values[node] == k:
        answer = depth 
        return 
    
    # 자식 노드 탐색 
    for child in tree[node]:
        dfs(child, depth+1, tree, values, k)

print(solution(tree, values, k))


# code reference: joonlab(1508) / backjoon(25511) / 알고리즘 분류: 그래프이론, 그래프탐색, 트리