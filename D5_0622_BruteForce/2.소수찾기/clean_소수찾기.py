from itertools import permutations


#prime_detector 짜는게 맘에 안ㄷㄻ
#prime_detedtor 가 brute force의 핵심 문제인듯 사실 그냥 저 코드로해도 돌아가긴한다. --> 시간초과 안뜸
#이문제는 들어오는 리스트가 몇개 안되니까 prime을 모아놓은리스트를 따로 만드는것보다 그냥 이게 낫지 않나?

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
    return cnt


def list_to_string(permu_list, r, num_list):

    for i in range(len(permu_list)):
        temp = ''
        for j in range(r):
            temp += permu_list[i][j]
        if int(temp) not in num_list:
            num_list.append(int(temp))
    return num_list


def make_permulist(numbers):
    permu_list, num_list = [],[]
    for _ in range(1, len(numbers) + 1):
        permu_list = list(permutations(numbers, _))
        num_list = list_to_string(permu_list, _, num_list)
    return num_list


def solution(numbers):
    answer = prime_detector(make_permulist(numbers))
    return answer

print(solution())