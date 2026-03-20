# 15829: 해싱

# 50점 
L = int(input())
S = input().strip()

ans = 0
for i in range(L):
    s = ord(S[i]) - ord('a') + 1
    ans += s*31**(i)%1234567891

print(ans)

# 100점


# code ref: backjoon(15829) / 알고리즘 분류: 구현, 문자열, 해싱