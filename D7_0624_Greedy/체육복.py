def solution(n, lost, reserve):
    set_l = list(set(lost) - set(reserve))
    set_r = list(set(reserve) - set(lost))

    cnt = n - len(set_l)

    for i in range(len(set_l)):
        print(cnt, set_l, set_r)
        if set_l[i] - 1 in set_r:
            set_r.remove(set_l[i] - 1)
            cnt += 1
        elif set_l[i] + 1 in set_r:
            set_r.remove(set_l[i] + 1)
            cnt += 1
    answer = cnt
    return answer