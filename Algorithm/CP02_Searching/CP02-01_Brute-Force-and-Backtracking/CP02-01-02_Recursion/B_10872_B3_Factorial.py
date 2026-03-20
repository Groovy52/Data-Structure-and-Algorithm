# 10872: 팩토리얼

n = int(input())

def f(n):

    if n==0 or n==1:
        return 1
    else:
        if n > 1:
            return n * f(n-1)

print(f(n))


# code ref: backjoon(10872) / 알고리즘 분류: 수학, 구현