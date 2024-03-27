from datetime import datetime

from ReadFile import read_File
from SortMethods.BubbleSort import bubble_sort
from SortMethods.InsertSort import insert_sort
from SortMethods.HeapSort import heapSort
from SortMethods.QuickSort import QuickSort


def main():
    Big = "DataFiles/SortBig.txt"
    Medium = "DataFiles/SortMedium.txt"
    Small = "DataFiles/SortSmall.txt"
    data = (read_File(Medium))
    bubble = bubble_sort
    insert = insert_sort
    heap = heapSort
    quick = QuickSort
    sortMethod = bubble
    start = datetime.now()
    sortedData = sortMethod(data, 6)
    end = datetime.now()
    for i in sortedData:
        print(i)
    print((end - start).total_seconds())


if __name__ == "__main__":
    main()
