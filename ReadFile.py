from datetime import datetime


def read_File(path):
    file = open(path, "r")
    data = []
    for line in [i.split(",") for i in str(file.read()).split("\n")][:-1]:
        data.append([int(line[0]), line[1], line[2], line[3], int(line[4]),
                     datetime(int(line[5].split(".")[2]), int(line[5].split(".")[1]), int(line[5].split(".")[0])),
                     float(line[-1])])
    return data
