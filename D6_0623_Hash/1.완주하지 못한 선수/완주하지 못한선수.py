import collections

def solution(participant, completion):
    answer = ''
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys()))
    return list(answer.keys())[0]