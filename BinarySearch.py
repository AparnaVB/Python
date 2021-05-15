def binary_search(arr, target):
    mn = 0
    mx = len(arr) - 1

    while mx >= mn:
        mid = (mn + mx) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            mx = mid - 1
        else:
            mn = mid + 1

    return None


arr = list(range(1, 26))
target = 25
print("Found target at index : {}".format(binary_search(arr, target)))
