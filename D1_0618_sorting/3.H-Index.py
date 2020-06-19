def solution(n,citations):
    answer = 0
    citations.sort()
    cnt = 0
    for i in range(citations[n-1]): #인용된횟수 H가 될값
        for j in range(n): #h번 이상 인용된 논문의 갯수
            if i>=citations[j] :
                cnt +=1
                if cnt > i :
                    continue
        print(i,":",cnt)
        cnt = 0
    return answer

a = [3,0,6,1,5,100]
n = len(a) #발표한논문수
solution(n,a)