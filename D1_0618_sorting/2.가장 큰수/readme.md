가장큰수
https://programmers.co.kr/learn/courses/30/lessons/42746

처음에는 숫자를 한자리씩 떼서 비교하려고 함
1차 : string으로 변환해서 소팅함 - 소팅 알고리즘이 별로였음
2차 : 퀵소트 알고리즘을 쓰려고 했는데 너무 어렵당...
3차 : 간단한 퀵소트 알고리즘을 짰다... 기 보다는 복붙했다

퀵소트 좀더 공부하는게 좋을듯!




1차코드 : 처음에 숫자를 한자리씩 뗴서 비교하려다가 스트링 비교로 하는것도 괜찮다 싶어서 해봤음
numbers는 숫자고 비교할때만 compare_by_string으로 이용했ㅇ미

"""
def digit(num, n) : 
    n = 10**n
    num = num %n 
    while True :     
        if n== 1 : return num
        n /= 10
        num = int(num/n)

def compare_by_string(a,b) : 
    str1 = str(a)+str(b)
    str2 = str(b)+str(a)
    if int(str1)> int(str2):
        return a
    else : return b
    
def swap (i,j,numbers):
    temp = numbers[i] 
    numbers[i] =numbers[j]
    numbers[j] = temp
    return numbers
    
def solution(numbers):
    answer = ''
    temp = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[j]==compare_by_string(numbers[i],numbers[j]):
                numbers = swap(i,j,numbers)            

    for _ in range(len(numbers)):
        answer += str(numbers[_])
                

    return answer
"""

테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (2379.60ms, 11.2MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	통과 (0.27ms, 10.9MB)
테스트 8 〉	통과 (0.14ms, 11MB)
테스트 9 〉	통과 (0.15ms, 11MB)
테스트 10 〉	통과 (0.15ms, 10.9MB)
테스트 11 〉	실패 (1.17ms, 11MB)

결과는 런타임 에러 및 실패

