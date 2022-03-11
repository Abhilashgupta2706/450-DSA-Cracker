import random

arr1 = [2, 0, 2, 1, 1, 0]
arr2 = [2, 0, 1]

arr3 = []


def randomFunc(arr):
    for nums in range(random.randint(5, 20)):
        arr.append(random.randint(0, 2))
    return arr


randomFunc(arr3)


def sortWithoutSortFunc(arr):
    # for i in range(len(arr)):
    #     for j in range(i + 1, len(arr)):
    #         if arr[i] > arr[j]:
    #             arr[i], arr[j] = arr[j], arr[i]

    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr


print(sortWithoutSortFunc(arr1))
print(sortWithoutSortFunc(arr2))
print(f'{arr3} -> ', sortWithoutSortFunc(arr3))
