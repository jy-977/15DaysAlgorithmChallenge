#remove [] each end of the string
def remove_brackets (array):
    str_arr = array.strip('[]')
    return str_arr

#make array and commands into int arrays
def process_input(array, commands) :
    array = remove_brackets(array)
    commands = remove_brackets(commands)

    array = list(map(int, array.split(',')))
    commands = commands.split('], [')
    temp = []
    for _ in range(len(commands)):
        temp.append(commands[_].split(', '))
        temp[_] = list(map(int, temp[_]))
    commands = temp
    return array,commands

def solution(array, commands):
    #make the elements right
    array, commands = process_input(array, commands)

    c_len = len(commands)
    answer = []
    for _ in range(c_len):
        temp = array[commands[_][0]-1:commands[_][1]]
        temp.sort()
        answer.append(temp[commands[_][2]-1])
    return answer


array = input()
commands = input()
print(solution(array, commands))
