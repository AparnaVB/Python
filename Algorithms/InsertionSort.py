def move_elememts(arr, start_index, value):
    # print("value at start index {0}, value {1}".format(arr[start_index], value))
    while start_index >= 0 and arr[start_index] > value:
        arr[start_index+1] = arr[start_index]
        # print("Array after moving {}".format(arr))
        start_index = start_index - 1
    arr[start_index+1] = value
    # print("Array after start index {0} - {1}".format(start_index+1,arr))
    return arr


def insertion_sort(arr):
    if len(arr) == 1:
        return arr
    for i in range(0, len(arr)-1):
        move_elememts(arr, i, arr[i+1])
    return arr


arr = [22, 11, 99, 88, 9, 7, 42]
print("Input Array  {}".format(arr))
print("Sorted Array {}".format(insertion_sort(arr)))
print("-"*50)
arr1 = [-9, 0, 5, 99, 11, 7, 42];
print("Input Array  {}".format(arr1))
print("Sorted Array {}".format(insertion_sort(arr1)))
