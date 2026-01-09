import sys
sys.setrecursionlimit(10**6)

n,k = map(int, input().split())
edges = list(list(map(int, input().split())) for _ in range(n-1))
values = list(map(int, input().split()))

ans = 0
e = [[] for _ in range(n)]
for i in range(n-1):
    p,c = edges[i]
    e[p].append(c)

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

# code reference: joonlab(1583)