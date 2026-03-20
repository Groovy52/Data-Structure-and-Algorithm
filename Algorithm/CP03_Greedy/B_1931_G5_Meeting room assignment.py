# 1931: 회의실 배정

n = int(input())
meetings = list()
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key = lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1 
        end_time = end 
print(count)

# code ref: backjoon(1931) / 알고리즘 분류: 그리디 알고리즘, 정렬