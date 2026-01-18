import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    p, c = map(int, input().split())
    tree[p].append(c)
values = list(map(int, input().split()))
answer = -1 

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


# code reference: joonlab(1508)