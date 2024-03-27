from datetime import datetime


def heapify(arr, n, i, index):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root

    if l < n and arr[i][index] < arr[l][index]:
        largest = l


    # See if right child of root exists and is
    # greater than root

    if r < n and arr[largest][index] < arr[r][index]:
        largest = r

    # Change root, if needed

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

        # Heapify the root.

        heapify(arr, n, largest, index)


# The main function to sort an array of given size

def heapSort(arr, index):
    start = datetime.now()
    n = len(arr)


    # Build a maxheap.
    # Since last parent will be at (n//2) we can start at that location.

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i, index)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0, index)

    end = datetime.now()
    return arr
