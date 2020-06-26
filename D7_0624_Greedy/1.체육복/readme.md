체육복 Lv.1
https://programmers.co.kr/learn/courses/30/lessons/42862

Definately, it's easy. But it took whole day to solve.
General algorith is so easy. But I couldn't find the exceptiona case.
I NEED TO READ THE PROBLEM PROPERLY.

and SET was first time for me. 
And I figure it out 
in the <for> loop if you define the range from 0 to len(list) when the length of list is keep changing
It's easy to get OutOfIndex Error. 

문제 자체는 쉬운데 푸는데 하루 웬종일 걸림 어이 X...
알고리즘도 엄청 간단한데 테스트 돌려서 안될때 예외케이스를못찾아서 맨날 힌트를 얻어서 푼다.
문제 좀 제대로 읽기!

그 SET도 첨써본건데 신박한듯 이거 없으면 훨씬 효율이 떨어진다 생각해놓자
파이썬은 이런 새로운 문법을 찾아보는데도 시간을 좀 잡아먹는거 같다
아직 나는 c로 생각하는게 더 많은듯
*주의
for 문돌때 range를 len(list)로 잡은 경우에 list길이가 계속변하면 out of index가 나기 쉬움
def solution(n, lost, reserve):
    set_l = list(set(lost)- set(reserve))
    set_r = list(set(reserve) - set(lost))
    
    cnt = n-len(set_l)     
    
    for i in range(len(set_l)):
        print(cnt,set_l, set_r)
        if set_l[i]-1 in set_r :
            set_r.remove(set_l[i]-1)
            cnt+=1
        elif set_l[i]+1 in set_r : 
            set_r.remove(set_l[i]+1)
            cnt+=1
    answer = cnt
    return answer