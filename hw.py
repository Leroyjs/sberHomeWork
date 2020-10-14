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


import re

#1

#2
data="de3u sds3dfs sdcds deu sdsdfs sdsdfs sd3cds "

def funcExercise2(string):
  if re.search(r'\b[a-zA-Z]+\b \b[a-zA-Z]+\b \b[a-zA-Z]+\b', string) is not None:
    return True
  return False

print("Ex2:",funcExercise2(data))

#3
data="ddeeeeedddddd222222222"

def funcExercise3(string):
  maxCount=0
  currentCount=0
  currentSymbol=False
  for i in list(string):
    if i == currentSymbol:
      currentCount+=1
    else:
      currentCount = 1
      currentSymbol= i
    if currentCount > maxCount:
        maxCount = currentCount
  return maxCount    

print("Ex3:",funcExercise3(data))

#4
data="ddHeeEeL L eOe=-=-234~_-+dddddd222222222"

def funcExercise4(string):
  correctString = ''
  for i in list(string):
    if re.search(r'[A-Z]', i) is not None:
      correctString+=i
  return correctString

print("Ex4:",funcExercise4(data))
