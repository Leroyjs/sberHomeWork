# 1
import re
array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print("Ex1:", array[0], array[2], array[-2])

# 2
array = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def funcExercise2(array, N):
    if len(array) < N:
        return -1
    return array[N-1]**N


print("Ex2:", funcExercise2(array, 9), funcExercise2(array, 10))

# 3
data = "sberrrrbank"


def funcExercise3(string, symbol):
    isFirst = True
    index = -1
    for i in list(string):
        index += 1
        if symbol == i:
            if isFirst == False:
                return index
            isFirst = False


print("Ex3:", funcExercise3(data, 'b'))

# 4
data = 10110011010000


def funcExercise4(number):
    divider = 10
    quantity = 0
    while number % divider == 0:
        divider *= 10
        quantity += 1
    return quantity


print("Ex4:", funcExercise4(data))

# 5
data = "sberbank"


def funcExercise5(string):
    return string[::-1]


print("Ex5:", funcExercise5(data))

# 6
array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
arraySecond = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def funcExercise6(array):
    firstElement = array[0]
    newArray = array[1:]
    isIdentical = True
    for i in newArray:
        if i == firstElement:
            isIdentical = False
    return isIdentical


print("Ex6:", funcExercise6(array), funcExercise6(arraySecond))

# 7

data = "defffffffffffffr4fHHf"


def funcExercise7(password):
    if re.search('^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{16,}$', password) is not None:
        return True
    return False


print("Ex7:", funcExercise7(data))

# 8
data = [1, [2, 2, [3], 2], ['dere', True, [[[[[[[[99999]]]]]]]]], [1], 4]


def funcExercise8(array):
    newArray = []

    for item in array:
        if isinstance(item, list):
            newArray.extend(funcExercise8(item))
        else:
            newArray.append(item)

    return newArray


print("Ex8:", funcExercise8(data))

# 9
data = {'a': 1.002, 'b': 1.001, 'c': 0.100, 'd': 999, }


def funcExercise9(dictionary):
    return max(dictionary, key=dictionary.get)


print("Ex9:", funcExercise9(data))

# 10
array = [1, 2, 3, 1, 3, 4, 4, 4, "4", "4", "1", [1], [1], [2]]


def funcExercise10(inputArray):
    outputArray = []
    for i in inputArray:
        if inputArray.count(i) >= 2:
            outputArray.append(i)
    return outputArray


print("Ex10:", funcExercise10(array))
