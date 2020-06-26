from math import gcd
def generator(arr):
    def lcm(x,y):
        return x* y // gcd(x,y)

    while True :
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr)==1:
            return arr[0]

def solution (arr):
    answer = generator(arr)
    return answer