arr1 = [1, 2, 3]
arr2 = [2, 1, 5, 4]
arr3 = ['B', 'O', 'S', 'S']


def reverse(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


print(reverse(arr1))
print(reverse(arr2))
print(reverse(arr3))
