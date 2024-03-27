from datetime import datetime


def bubble_sort(list, index):
    switch = True

    start = datetime.now()
    while switch:
        switch = False
        for i in range(len(list) - 1):
            if list[i][index] > list[i + 1][index]:
                list[i], list[i + 1] = list[i + 1], list[i]
                switch = True

    end = datetime.now()
    # time = (end - start).total_seconds()
    return list
