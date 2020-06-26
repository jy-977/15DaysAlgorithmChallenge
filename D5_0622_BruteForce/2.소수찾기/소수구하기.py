from itertools import permutations


def prime_detector(num_list):
    cnt = 0
    check = 0
    for num in num_list:
        if num != 1 and num != 0:
            for divider in range(2, num):
                if num % divider == 0:
                    check += 1
                    break
            if check == 0:
                cnt += 1
        # init
        check = 0
    print(cnt)
    return cnt


def list_to_string(permu_list, r, num_list):
    temp = ''
    for i in range(len(permu_list)):
        for j in range(r):
            temp += permu_list[i][j]
        if int(temp) not in num_list:
            num_list.append(int(temp))
        temp = ''
    return num_list


def make_permulist(numbers):
    permu_list = []
    num_list = []
    # 순열을 찾음
    for _ in range(1, len(numbers) + 1):
        permu_list = list(permutations(numbers, _))
         # 숫자로 바꿔서 넣음
        num_list = list_to_string(permu_list, _, num_list)
    return num_list


def solution(numbers):
    answer = 0
    temp = make_permulist(numbers)
    answer = prime_detector(temp)
    return answer