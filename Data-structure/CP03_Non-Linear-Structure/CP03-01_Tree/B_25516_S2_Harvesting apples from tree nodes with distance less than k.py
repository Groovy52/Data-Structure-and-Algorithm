# 25516: 거리가 k이하인 트리 노드에서 사과 수확하기

# 1)
import sys
sys.setrecursionlimit(10**6)

n,k = map(int, input().split())
edges = list(list(map(int, input().split())) for _ in range(n-1))
values = list(map(int, input().split()))
e = [[] for _ in range(n)]
for i in range(n-1):
    p,c = edges[i]
    e[p].append(c)

ans = 0

def solution(tree, k, values):
    global ans 
    # cu node, cur depth, tree, k, values
    dfs(0, 0, tree, k, values)
    return ans 

def dfs(u, depth, tree, target_depth, apples):
    global ans 
    if depth > k:
        return 
    ans += apples[u]
    
    for child in tree[u]:
        dfs(child, depth+1, tree, target_depth, apples)
        
print(solution(e, k, values))

# 2)
import sys 
sys.setrecursionlimit(10**6)

n,k = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)
num_apples = list(map(int, input().split()))

def dfs(node, dist):
    if dist > k:
        return 0
        
    total= num_apples[node]
    
    for child in tree[node]:
        total += dfs(child, dist + 1)
    return total

print(dfs(0,0))

# code reference: joonlab(1583) / backjoon(25516) / 알고리즘 분류: 그래프이론, 그래프탐색, 너비우선탐색, 깊이우선탐색, 트리