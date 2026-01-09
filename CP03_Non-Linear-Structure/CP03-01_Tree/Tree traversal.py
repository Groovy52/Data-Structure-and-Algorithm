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
# preorder('A')
# inorder('A')
# postorder('A')

# print(result_pre)
# print(result_in)
# print(result_post)

# code reference: BACKJOON ONLINE JUDGE(1991)