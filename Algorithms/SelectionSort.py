def selection_sort(arr):
    if len(arr) > 1:
        for i in range(0, len(arr)-1):
            min_index = find_min(arr, i)
            swap_elements(arr, i, min_index)
    return arr


def find_min(arr, start_index):
    min_value = arr[start_index]
    min_index = start_index
    for i in range(start_index+1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
    return min_index


def swap_elements(arr, index1, index2):
    temp = arr[index2]
    arr[index2] = arr[index1]
    arr[index1] = temp


arr = [22, 11, 99, 88, 9, 7, 42]
print("Current array " + ", ".join(map(str, arr)))
print("Sorted array " + ", ".join(map(str, selection_sort(arr))))
print("-"*40)
arr1 = [6, 3, 10, 0, -1]
print("Current array " + ", ".join(map(str, arr1)))
print("Sorted array " + ", ".join(map(str, selection_sort(arr1))))
