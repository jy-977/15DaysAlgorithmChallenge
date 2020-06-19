#check : 값 저장하는 list

cnt = 0

def dfs(idx, check,numbers,target):
    global cnt
    for i in range(2):
        if i == 0:
            np = 1
        else:
            np = -1
        if 0<= idx < len(numbers):
            check.append(numbers[idx] * np)
            #값 체크
            if idx==len(numbers)-1:
                if sum(check) == target:
                    cnt += 1
            dfs(idx+1,check,numbers,target)
            check.pop()

    return cnt

def solution(numbers, target):
    answer = 0
    check = []
    answer = dfs(0, check, numbers, target)
    return answer