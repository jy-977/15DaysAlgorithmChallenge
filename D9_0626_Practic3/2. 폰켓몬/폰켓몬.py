def solution(nums):
    answer = 0
    n = int(len(nums)/2)
    nums = list(set(nums))
    print(nums)
    if len(nums)< n:
        answer = len(nums)
    else :
        answer = n