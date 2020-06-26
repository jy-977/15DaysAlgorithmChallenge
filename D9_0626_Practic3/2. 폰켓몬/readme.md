폰켓몬 Lv.2
https://programmers.co.kr/learn/courses/30/lessons/1845

There's no specific algorithm for this
just keep in mind to reduce the time complexity

In first try, I tried to use combinations() == >totally not good for time 
and compare the combination
==> procedure based
<source code v1>
"from itertools import combinations
def solution(nums):
    answer = 0
    n = int(len(nums)/2)
    nums=list(combinations(nums, n))
    for i in range(len(nums)):
        check = []
        part_max = 0
        for j in range(len(nums[i])):
            print(check)
            if nums[i][j] not in check :
                check.append(nums[i][j])
                part_max+=1
        answer = max(part_max, answer)
    return answer"

In second try, remove the duplicatd elements and compare with the numbers
==> more intuitive 

난이도 낮은 문제 근데 시간 초과를 어떻게 줄이느냐가 관건
처음에는 문제처럼 따라가려고 했음 조합 맞춰서 비교하는 방법으로 
근데 데이터범위가 큰게 시간초과 문제임을 알고 방법을 바꿨음

두번째는 숫자를 비교하는 걸로 바꿨음 element 중복 없애서 숫자 비교하는걸로 --> 직관적