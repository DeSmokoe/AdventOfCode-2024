def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(data):
    my_file = readfile(data)
    data = my_file.split("\n")

    # split every number into two numbers
    data = [x.split(" ") for x in data]

    # turn string into int
    data = [[int(x) for x in y] for y in data]

    return data