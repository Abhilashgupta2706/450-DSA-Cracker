a1, b1 = [18, 17, 13, 12, 14, 11, 11, 10, 12], [16, 13, 14, 13, 15, 11, 12, 10, 19, 10]


def intersection(arr1, arr2, output_arr):
    for ele in arr1:
        if ele in arr2 and ele not in output_arr:
            output_arr.append(ele)
    for ele in arr2:
        if ele in arr1 and ele not in output_arr:
            output_arr.append(ele)
    return output_arr


def union(a, b, output_arr):
    for i in a:
        for j in b:
            if i not in output_arr:
                output_arr.append(i)
            elif j not in output_arr:
                output_arr.append(j)
    return output_arr


def unionAndIntersection(a, b):
    union_arr = []
    intersection_arr = []

    union(a,b, union_arr)
    intersection(a, b, intersection_arr)

    result1 = len(union_arr)
    result2 = len(intersection_arr)
    return result1, result2


print(unionAndIntersection(a1, b1))
