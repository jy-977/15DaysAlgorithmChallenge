min_length = 100

#두 문자열 글자 다른거 반환 0: 같은문자 / 1:한글자만 다른문자 / -1:
def c_detector(word1, word2):
    cnt= 0
    for _ in range(len(word1)):
        if word1[_]!=word2[_]:
            cnt+=1
    if cnt == 0 : return 0
    elif cnt ==1 : return 1
    else : return -1

def dfs(start, words, target, stack) :
    global min_length
    for i in range(start+1, len(words)):
        #if 한글자만 다르면
        if  c_detector(words[start], words[i]) == 1:
            stack.append(words[i])
            print(stack)
            if words[i] == target: #찾았을때만 바꿔야함
                min_length = min(len(stack),min_length)

            dfs(i, words, target, stack)
            stack.pop()


def solution(begin, target, words):
    global min_length
    #words.insert(0,begin)
    stack=[]
    dfs(0,words, target,stack)
    if min_length > 50 : min_length = 0
    answer = min_length
    return answer
