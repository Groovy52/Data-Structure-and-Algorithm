# ============================= 1) 
N = int(input())
T = dict()
for _ in range(N):
    prt, child_l, child_r = input().split()
    T[prt] = (child_l, child_r)

result_pre = ''
def preorder(node):
    global result_pre
    if node == '.': # 자식 노드가 더이상 없으면 함수 종료 
        return
    result_pre += node 
    preorder(T[node][0])
    preorder(T[node][1])

result_in = ''
def inorder(node):
    global result_in
    if node == '.':
        return 
    inorder(T[node][0])
    result_in += node 
    inorder(T[node][1])
    
result_post = ''
def postorder(node):
    global result_post
    if node == '.':
        return 
    
    postorder(T[node][0])
    postorder(T[node][1])
    result_post += node 


# 반드시 선언 후 결과값 출력, 선언 x => 결과값: None
preorder('A')
inorder('A')
postorder('A')

print(result_pre)
print(result_in)
print(result_post)


# ============================= 2) 

n = int(input())
nodes = list(list(input().split()) for _ in range(n))

tree = {}
for p, l, r in nodes:
    tree[p] = (l, r)

def pre_order(node):
    if node == '.':
        return
    print(node, end='')
    pre_order(tree[node][0])
    pre_order(tree[node][1])
    
def in_order(node):
    if node == '.':
        return
    in_order(tree[node][0])
    print(node, end='')
    in_order(tree[node][1])

def post_order(node):
    if node == '.':
        return
    post_order(tree[node][0])
    post_order(tree[node][1])
    print(node, end='')
    
    
pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()


# ============================= 3) 
n = int(input())
nodes = list(list(input().split()) for _ in range(n))

tree = {}

for p, l, r in nodes:
    tree[p] = (l, r)

def pre_order(node):
    if node == '.':
        return ''
    return node + pre_order(tree[node][0]) + pre_order(tree[node][1])
    
def in_order(node):
    if node == '.':
        return ''
    return in_order(tree[node][0]) + node + in_order(tree[node][1])

def post_order(node):
    if node == '.':
        return ''
    return post_order(tree[node][0]) + post_order(tree[node][1]) + node
    
print(pre_order('A'))
print(in_order('A'))
print(post_order('A'))



# code reference: backjoon (1991) / 알고리즘 분류: 트리, 재귀