# 11723: 집합

import sys
input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    cmd = input().split()

    if cmd[0] == 'add':
        x = int(cmd[1])
        S |= (1 << (x - 1))

    elif cmd[0] == 'remove':
        x = int(cmd[1])
        S &= ~(1 << (x - 1))

    elif cmd[0] == 'check':
        x = int(cmd[1])
        if S & (1 << (x - 1)):
            print(1)
        else:
            print(0)

    elif cmd[0] == 'toggle':
        x = int(cmd[1])
        S ^= (1 << (x - 1))

    elif cmd[0] == 'all':
        S = (1 << 20) - 1

    elif cmd[0] == 'empty':
        S = 0
        

# code ref: backjoon(11723) / 알고리즘 분류: 구현, 집합과 맵, 비트마스킹