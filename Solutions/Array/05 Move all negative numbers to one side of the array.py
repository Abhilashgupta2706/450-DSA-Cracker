arr1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr2 = [1, 2, -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2, 1]


def moveNegativeInt(arr):
    for i in arr:
        if i < 0:
            temp = i
            arr.remove(i)
            arr.insert(0, temp)
    return arr


print(moveNegativeInt(arr1))
print(moveNegativeInt(arr2))
