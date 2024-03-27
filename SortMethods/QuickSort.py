from datetime import datetime


def quicksort(arr, index):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][index]
    left = [x for x in arr if x[index] < pivot]
    middle = [x for x in arr if x[index] == pivot]
    right = [x for x in arr if x[index] > pivot]
    return quicksort(left, index) + middle + quicksort(right, index)


def QuickSort(arr, index):
    start = datetime.now()
    result = quicksort(arr, index)
    end = datetime.now()
    return result



