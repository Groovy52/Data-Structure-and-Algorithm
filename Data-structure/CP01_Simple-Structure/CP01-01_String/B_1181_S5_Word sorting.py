# 1181: 단어 정렬
N = int(input())
str_list = []
for _ in range(N):
    string = input().strip()
    str_list.append(string)

str_list = list(set(str_list))
str_list.sort()
str_list.sort(key = lambda x: len(x))

for s in str_list:
    print(s)


# code ref: backjoon(1181) / 알고리즘 분류: 문자열, 정렬