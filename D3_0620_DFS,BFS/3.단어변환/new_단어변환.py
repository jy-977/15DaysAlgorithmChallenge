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
    for i in range(len(words)): #idx에 남아있는 만큼만 돌아야함
        print("\n\nstart : ", start,"i : ", i, "len(words):", len(words))
        #if 한글자만 다르면
        if  c_detector(start, words[i]) == 1 or c_detector(start, words[i] )==0:
            stack.append(words[i])
            words.remove(words[i])
            print("stack: ",stack)
            print("words: ",words)

            if words[i] == target: #찾았을때만 바꿔야함
                min_length = min(len(stack),min_length)
                print("min length : ",min_length,"min:", len(stack))
            dfs(stack[len(stack)-1], words, target, stack)
    a= stack.pop()
    words.append(a)
    print("fail to reach end")
           # idx.append()

def solution(begin, target, words):
    global min_length
    stack=[]
    idx = []
    for _ in range(len(words)-1):
        idx.append(_)
    dfs(begin,words, target,stack)
    if min_length > 50 : min_length = 0
    answer = min_length
    return answer

print(solution("hit","cog",["hot","dot","dog","lot","log","cog"]))
