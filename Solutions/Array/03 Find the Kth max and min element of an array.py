import random

arr1, k1 = [7, 10, 4, 3, 20, 15], 3
arr2, k2 = [7, 10, 4, 20, 15], 4


def randomNum(arr):
    for i in range(0, random.randint(4, 15)):
        arr.append(random.randint(0, 100))
    return arr


arr3 = []
randomNum(arr3)
k3 = random.randint(1, len(arr3))


def kthMinMaxNum(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    min_num, max_num = arr[k - 1], arr[-k]
    return f'{arr} -> (Min, Max) = ({min_num},{max_num}) '


print(kthMinMaxNum(arr1, k1))
print(kthMinMaxNum(arr2, k2))
print(kthMinMaxNum(arr3, k3), f'Where k is {k3}')
