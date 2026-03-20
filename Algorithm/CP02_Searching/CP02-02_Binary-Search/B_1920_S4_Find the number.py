# 1920: 수 찾기

# 시간 초과 코드: 원인 sort() 반복
def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True 
        elif data[mid] > target:
            end = mid -1 
        else:
            start = mid + 1
    return 

N = int(input())
N_li = list(map(int, input().split()))
M = int(input())
M_li = list(map(int, input().split()))

for n in M_li:
    if binary_search(n, N_li):
        print(1)
    else:
        print(0)

# 에러 미발생 코드
def binary_search(target, data):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True 
        elif data[mid] > target:
            end = mid -1 
        else:
            start = mid + 1
    return 

N = int(input())
N_li = list(map(int, input().split()))
N_li.sort()
M = int(input())
M_li = list(map(int, input().split()))

for n in M_li:
    if binary_search(n, N_li):
        print(1)
    else:
        print(0)


# code ref: backjoon(1920) / 알고리즘 분류: 자료구조, 정렬, 이분탐색, 집합과 맵, 해시를 사용한 집합과 맵