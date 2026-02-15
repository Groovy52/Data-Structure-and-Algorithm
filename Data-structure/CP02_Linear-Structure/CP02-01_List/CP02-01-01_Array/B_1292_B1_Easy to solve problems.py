"""
1292: 쉽게 푸는 문제
"""

# n*(n+1)/2 = 1000

s, e = map(int, input().split())

i = 0
num_list = []
while i <= 45:
    num_list.extend([i]*i)
    i+=1
    
print(sum(num_list[s-1:e]))


# code ref: backjoon(1292) / 알고리즘 분류: 수학, 구현
