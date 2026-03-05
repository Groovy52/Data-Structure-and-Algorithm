# 1120: 조건에 맞는 정수의 개수 (Small2)

# 틀린 코드

n = int(input())


def is_ok(num):
    if num == 0 or (num%10)==0:
        ans = False
    else:
        p = num % 10
        c = (num//10) % 10

        if abs(p-c) <= 2:
            ans = True
            return is_ok(num // 10)
        else:
            ans = False
            
    return ans


def solution(n):
    if n==1:
        return 9
    
    else:
        count = 0
        for num in range(10**(n-1), 10**n):

            if is_ok(num):
                print(num)
                count += 1

        return count
    
solution(3)