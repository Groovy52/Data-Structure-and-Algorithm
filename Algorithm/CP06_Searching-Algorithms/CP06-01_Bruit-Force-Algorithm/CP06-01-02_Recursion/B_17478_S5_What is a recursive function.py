# 17478: 재귀함수가 뭔가요? 

n = int(input())

base_str = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
recurr_1_str = '"재귀함수가 뭔가요?"'
recurr_2_str = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
recurr_3_str = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
recurr_4_str = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

end_1_str = '"재귀함수가 뭔가요?"'
end_2_str = '"재귀함수는 자기 자신을 호출하는 함수라네"'

end_recurr_str = "라고 답변하였지."

def recurr(depth):
    if depth==n:
        print("____"*depth+end_1_str)
        print("____"*depth+end_2_str)
        print("____"*depth+end_recurr_str)

        
        return
    else:
        print("____"*depth+recurr_1_str)
        print("____"*depth+recurr_2_str)
        print("____"*depth+recurr_3_str)
        print("____"*depth+recurr_4_str)

    recurr(depth+1)
    print("____"*depth+end_recurr_str)

print(base_str)
recurr(0)


# code ref: backjoon(17478) / 알고리즘 분류: 구현, 재귀