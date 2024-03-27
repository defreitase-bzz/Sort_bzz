from datetime import datetime


def insert_sort(list, index):
    start = datetime.now()
    for i in range(len(list)-1):
        pos, min = i, list[i][index]
        for j in range(i + 1, len(list)):
            if list[j][index] < min:
                min = list[j][index]
                pos = j
        list[i], list[pos] = list[pos], list[i]
    end = datetime.now()
    print('insertsort')
    return list