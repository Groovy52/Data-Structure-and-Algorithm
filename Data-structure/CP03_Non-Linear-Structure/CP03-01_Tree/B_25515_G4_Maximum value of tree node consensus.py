# 25515: 트리 노드 합의 최댓값

# 1) 
import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)

values = list(map(int, input().split()))

def solution(tree, values):
    return get_totalsum(0, tree, values)

def get_totalsum(node, tree, values):
    total = values[node]

    for child in tree[node]:
        gain = get_totalsum(child, tree, values)

        if gain > 0:
            total += gain 
    
    return total

print(solution(tree, values))

# 2)
import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)

values = list(map(int, input().split()))

def dfs(node):
    res = values[node]

    for child in tree[node]:
        res += max(dfs(child), 0)

    return res

print(dfs(0))

# code ref: joonlab(1582) / backjoon(25515) / 알고리즘 분류: 그래프이론, 그래프탐색, 깊이우선탐색, 트리, 동적계획법, 트리동적계획법
