def solution(brown, yellow):
    answer = []
    for a in range(1,yellow+1):
        b = int(yellow/a)
        if yellow == a*b :
            if brown == (2*a + 2*b +4):
                print("a: ",a, "b: ", b)
                if a<b : a,b = b,a
                answer = [a+2, b+2]

    return answer