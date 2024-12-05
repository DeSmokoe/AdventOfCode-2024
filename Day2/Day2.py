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

# do three safety checks
# 1. check if the abs difference of all subsequent numbers is between 1 and 3
# 2. check if all subsequent numbers are consistently increasing OR decreasing (can't be both)

def check_safety(data):
    data = dataprep(data)
    unsafe_reports = []

    for j in range(len(data)):
        momentum = "increase" if data[j][0] < data[j][1] else "decrease"
        for i in range(len(data[j]) - 1):
            new_momentum = "increase" if data[j][i] < data[j][i + 1] else "decrease"
            if abs(data[j][i] - data[j][i + 1]) not in [1, 2, 3]:
                unsafe_reports.append(j+1)
                break
            if new_momentum != momentum:
                unsafe_reports.append(j+1)
                break

    return len(data) - len(unsafe_reports)

# Part 1
# print(check_safety("Test.txt"))
# print(check_safety("Puzzle.txt"))


def check_safety_advanced(data):
    data = dataprep(data)
    unsafe_reports = []
    counter = 0

    for j in range(len(data)):
        momentum = "increase" if data[j][0] < data[j][1] else "decrease"
        for i in range(len(data[j]) - 1):
            new_momentum = "increase" if data[j][i] < data[j][i + 1] else "decrease"
            if abs(data[j][i] - data[j][i + 1]) not in [1, 2, 3]:
                if not problem_dampler(data[j], i):
                    unsafe_reports.append(j + 1)
                    break
            if new_momentum != momentum:
                if not problem_dampler(data[j], i):
                    unsafe_reports.append(j + 1)
                    break

    return len(data) - len(unsafe_reports)

def problem_dampler(data_row, problem_level):
    # remove problem level from data row
    counter = 0

    #one by one remove each number and check if the data row is still safe
    for j in range(len(data_row)):
        counter = 0
        shortened_data_row = data_row[:j] + data_row[j+1:]

        momentum = "increase" if shortened_data_row[0] < shortened_data_row[1] else "decrease"
        # check if the abs difference of all subsequent numbers is between 1 and 3
        for i in range(len(shortened_data_row) - 1):
            new_momentum = "increase" if shortened_data_row[i] < shortened_data_row[i + 1] else "decrease"
            if abs(shortened_data_row[i] - shortened_data_row[i + 1]) not in [1, 2, 3]:
                break
            elif new_momentum != momentum:
                break
            elif i == len(shortened_data_row) - 2:
                return True


# Part 2
print(check_safety_advanced("Test.txt"))
print(check_safety_advanced("Puzzle.txt"))
