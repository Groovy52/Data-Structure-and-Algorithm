# 2606: 바이러스

# 1) ?? 잘 이해 x
N = int(input())
P = int(input())
pairs = list(list(map(int, input().split())) for _ in range(P))

edges = [[] for _ in range(N+1)]
for a, b in pairs:
    edges[a].append(b)
    edges[b].append(a)

visited = [False]*(N+1)

def dfs(node):
    visited[node] = True
    linked = 0

    for nxt_node in edges[node]:
        if not visited[nxt_node]:
            linked += 1 # 본인이 감염시킨
            linked += dfs(nxt_node) # 본인+ 자식이 감염시킨
    
    return linked

print(dfs(1))

# 2) 
N = int(input())
P = int(input())
pairs = list(list(map(int, input().split())) for _ in range(P))

edges = [[] for _ in range(N+1)]
for a, b in pairs:
    edges[a].append(b)
    edges[b].append(a)

visited = [False]*(N+1)

global linked
linked = -1
def dfs(node):
    visited[node] = True
    global linked
    linked += 1

    for nxt_node in edges[node]:
        if not visited[nxt_node]:
            dfs(nxt_node)
    
dfs(1)
print(linked)


# code ref: backjoon(2606) / 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색