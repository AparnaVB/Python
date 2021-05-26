def sort(arr, start, end):
    if len(arr[start:end]) == 1:
        return arr[0]
    else:
        mid = (start+end)//2
        sort(arr, start, mid)
        sort(arr, mid, end)
        merge(arr, start, end)
    return arr


def merge(arr, start, end):
    mid = (end + start) // 2
    left = arr[start:mid]
    right = arr[mid:end]
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[start] = left[i]
            i += 1
        else:
            arr[start] = right[j]
            j += 1
        start += 1
    if j >= len(right):
        while i < len(left):
            arr[start] = left[i]
            i += 1
            start += 1
    else:
        while j < len(right):
            arr[start] = right[j]
            j += 1
            start += 1


arr = [5, 4, 3, 2, 1]
print("Array before merge {}".format(arr))
print("Array after merge {}".format(sort(arr, 0, len(arr))))
print('-'*50)
arr = [6, 5, 4, 3, 2, 1]
print("Array before merge {}".format(arr))
print("Array after merge {}".format(sort(arr, 0, len(arr))))
print('-'*50)
arr = [6, 5, 0, 3, -2, 1]
print("Array before merge {}".format(arr))
print("Array after merge {}".format(sort(arr, 0, len(arr))))
