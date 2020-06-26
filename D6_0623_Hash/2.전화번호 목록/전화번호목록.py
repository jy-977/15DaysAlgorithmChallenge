def solution(phone_book):
    answer = True
    a = []
    a= sorted(phone_book,key=len)
    for i in range(len(a)) :
        for j in range(i+1,len(a)):
            print(a[i], a[j])
            if a[j].startswith(a[i]):
                answer = False
                return answer
    return answer