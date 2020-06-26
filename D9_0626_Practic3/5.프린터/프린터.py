import collections
def solution(priorities, location):
    priorities = collections.deque(priorities)
    cur = location
    answer =location
    zero_p= 0
    while True:
        zero_p = priorities.popleft()
        if not priorities :break
        if max(priorities)>zero_p :
            if cur == 0 :
                answer+=len(priorities)
                cur +=len(priorities)
            else :
                cur -= 1
                answer -=1
            priorities.append(zero_p)
        else :
            if cur== 0: break
            cur -=1
            continue
    return answer+1