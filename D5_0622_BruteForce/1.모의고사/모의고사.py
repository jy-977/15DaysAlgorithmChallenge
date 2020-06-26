def check_answer(answer, firstman, secondman, thirdman):
    check = [0, 0, 0]
    for i in range(len(answer)):
        if answer[i] == firstman[i % len(firstman)]:
            check[0] += 1
        if answer[i] == secondman[i % len(secondman)]:
            check[1] += 1
        if answer[i] == thirdman[i % len(thirdman)]:
            check[2] += 1

    return check


def rank(check):
    max_a = -1
    named = []
    for i in range(len(check)):
        max_a = max(max_a, check[i])
    for i in range(len(check)):
        if check[i] == max_a:
            named.append(i + 1)
    return named


def solution(answers):
    answer = []
    check = []
    firstman = [1, 2, 3, 4, 5]
    secondman = [2, 1, 2, 3, 2, 4, 2, 5]
    thirdman = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    check = check_answer(answers, firstman, secondman, thirdman)
    answer = rank(check)
    return answer