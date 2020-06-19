# return bigger one
def compare(a,b) :
    str1 = a+b
    str2 = b+a
    if int(str1) > int(str2):
      #  print(a, 1)
        return 1
    elif int(str1) < int(str2):
       # print(b, 2)
        return 2
    else : return 0

def swap(i, j, numbers):
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp
    return numbers


def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):

        pivot = arr[(low + high) // 2]
        print('\n\n pivot : ', pivot)
        while low <= high:
            #while arr[low]<pivot  A<B:
            while compare(arr[low], pivot) == 2:
                low += 1
            print('\n')
            while compare(arr[high], pivot) == 1:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high + 1
        return low

    return sort(0, len(arr) - 1)

def easy_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        #num < pivot
        if compare(num, pivot) == 2:
            greater_arr.append(num)
        #num > pivot
        elif compare(num, pivot) == 1:
            lesser_arr.append(num)
        #num == pivot
        else:
            equal_arr.append(num)
    return easy_quick_sort(lesser_arr) + equal_arr + easy_quick_sort(greater_arr)


def solution(numbers):
    answer = ''
    temp = []
    for _ in range(len(numbers)):
        numbers[_] = str(numbers[_])

    temp = easy_quick_sort(numbers)
    for _ in temp:
        answer+=_
    return answer

print(solution([6,10,2]))