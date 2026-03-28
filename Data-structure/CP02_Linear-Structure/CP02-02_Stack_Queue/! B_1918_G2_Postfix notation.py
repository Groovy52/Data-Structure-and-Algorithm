# 1918: 후위 표기식
cmd = list(input())

ans, stack = [], []
for a in cmd:
    if a.isalpha():
        ans.append(a)
    else:
        if a == '(':
            stack.append(a)
        elif a == '*' or a == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans.append(stack.pop())
            stack.append(a)
        elif a == '+' or a == '-' or a == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            if a != ')':
                stack.append(a)
            else:
                stack.pop()

while stack:
    ans.append(stack.pop())

print(''.join(map(str, ans)))


# code ref: backjoon(1918) / 알고리즘 분류: 자료 구조, 스택