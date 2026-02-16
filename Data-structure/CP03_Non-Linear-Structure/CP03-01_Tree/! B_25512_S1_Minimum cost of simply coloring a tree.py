# 25512: 트리를 간단하게 색칠하는 최소 비용

# 1) 
import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    p,c = map(int, input().split())
    tree[p].append(c)
cost = list(list(map(int, input().split())) for _ in range(n))

def solution(n, tree, cost):
    answer = []
    for i in range(2):
        global color_cost
        color_cost = 0
        dfs(i, 0, tree, cost)
        answer.append(color_cost)

    return min(answer)

def dfs(start_color, node, tree, cost):
    """
    DFS가 실제 존재하지 않는 노드(None)까지 호출되기 때문에
    잘못된 cost 접근과 트리 탐색을 막기 위한 Base Case(재귀 종료 조건)
    
    tree = {
    0: [1, 2],
    1: [3, None],   # ← 이런 값 들어가면 반드시 필요
    2: [],
    3: []
    }

    tree = {
    0: [1,2],
    1: [3],
    2: [],
    3: []
    }
    이때는 이 종료조건이 필요없으나, 시험/코테관점에서는 필요함.
    """
    if node==None:
        return 
    
    global color_cost
    color_cost += cost[node][start_color]
    
    for child in tree[node]:
        dfs(int(not(bool(start_color))), child, tree, cost)


print(solution(n, tree, cost))

# 2) !!이 코드는 준랩에선 통과지만, 백준에선 시간초과 발생

import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    p,c = map(int, input().split())
    tree[p].append(c)
cost = list(list(map(int, input().split())) for _ in range(n))

def solution(n, tree, cost):
    return min(dfs(0, 0, tree, cost), dfs(1, 0, tree, cost))

def dfs(start_color, node, tree, cost):
    if node==None:
        return
    
    color_cost = cost[node][start_color]

    for child in tree[node]:
        color_cost += dfs(int(not(bool(start_color))), child, tree, cost)
    
    return color_cost


print(solution(n, tree, cost))


# 3) !!이 코드는 준랩에선 통과지만, 백준에선 시간초과 발생
import sys
sys.setrecursionlimit(10**6)

def solution(n, A, edges):
    E = list([] for _ in range(n))
    for p, c in edges:
        E[p].append(c)
        
    return min(solve(0,0,A,E), solve(0,1,A,E))

def solve(u, color, A, E):
    ret = A[u][color]
    for v in E[u]:
        ret += solve(v, 1-color, A, E)
    
    return ret

n = int(input())
edges = list(list(map(int, input().split())) for _ in range(n-1))
A = list(list(map(int, input().split())) for _ in range(n))
print(solution(n, A, edges))

# code reference: joonlab(1509) / backjoon(25512) / 알고리즘 분류: 그래프이론, 그래프탐색, 이분그래프