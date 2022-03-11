import random

arr1 = [5, 7, 2, 4, 9, 6]


def randomNum(arr):
    for i in range(0, random.randint(4, 15)):
        arr.append(random.randint(0, 100))
    return arr


arr2 = []
randomNum(arr2)
arr3 = []
randomNum(arr3)


def maxMinNumber(arr):
    min_num, max_num = arr[0], arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i
    return min_num, max_num


print(arr1, '\n', maxMinNumber(arr1))
print(arr2, '\n', maxMinNumber(arr2))
print(arr3, '\n', maxMinNumber(arr3))
