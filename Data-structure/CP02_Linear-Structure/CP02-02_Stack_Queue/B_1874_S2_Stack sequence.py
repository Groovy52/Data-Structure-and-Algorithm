# 1874: 스택 수열

n = int(input())
stack = []
result = []

current = 1

for _ in range(n):
    num = int(input())

    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit()

print('\n'.join(result))


# code ref: backjoon(1874) / 알고리즘 분류: 자료구조, 스택