arr1, n1 = [1, 2, 3, 4, 5], 5
arr2, n2 = [9, 8, 7, 6, 4, 2, 1, 3], 8
arr3, n3 = [1, 8, 7, 5, 6, 7, 8, 7], 8


def rotate(arr, n):
    temp = arr[n - 1]
    arr.pop(n-1)
    arr.insert(0, temp)
    return arr


print(rotate(arr1, n1))
print(rotate(arr2, n2))
print(rotate(arr3, n3))
