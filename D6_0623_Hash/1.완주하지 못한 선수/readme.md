완주하지 못한 선수Lv.1
https://programmers.co.kr/learn/courses/30/lessons/42576

looks Easy but not easy.
if you don't know about collections.Counter or this kinda hashable object, there's no way to solve
I tried to check with "in", "remove" but it works like 'for' loop
So the time complexity is O(n^2) or more (not sure)
Especiall, due to "remove", in worst case O(n^2) can be possible

According to some reference code, THere are collections.Counter or sort, zip
I guess sort, sorted() are not the exact method

*import collections
return type of collections.Counter() ==> dictionary
so you need to focus on how to make dictionary to string
list(collections.COunter())[0]


문제 자체는 쉬운데 그 hashable 객체나 그런 함수같은거 모르면 못품
내가 푼거는 for 문 돌려서 in 써가지고 있나 확인한 다음에 remove로 제거했는데
이게 for문이랑 다름없게 돌아가서 time complexity가 O(n^2)됨
--> 효율성 엄청 떨어짐

그래서 그냥 collections.Counter 쓰거나 sor해서 찾는는데
sort도 딱히 답은아닌듯

"""
def solution(participant, completion):
    answer = ''
    for _ in completion :
        if _ in participant : 
            participant. remove(_)
    answer = str(participant)
    return answer
"""