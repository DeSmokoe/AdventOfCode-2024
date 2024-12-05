def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(data):
    my_file = readfile(data)
    data = my_file.split("\n")

    # split every number into two numbers
    data = [x.split("   ") for x in data]

    # turn string into int
    data = [[int(x) for x in y] for y in data]

    # transpose array
    data = list(map(list, zip(*data)))

    return data


def sort_low_to_high(data):
    data = dataprep(data)

    # sort the data
    data = [sorted(x) for x in data]

    return data

def calculate_difference(data):
    data = sort_low_to_high(data)
    difference = []

    for i in range(len(data[0])):

        difference.append(abs(data[0][i] - data[1][i]))

    return sum(difference)


# Part 1
print("Part 1")
print("----------------")
print("Test: " + str(calculate_difference("Test.txt")))
print("puzzle: " + str(calculate_difference("Puzzle.txt")))
print("\n")


def calculate_similarity(data):
    similarity_scores = []
    data = sort_low_to_high(data)

    for i in range(len(data[0])):
        # check how often this int appears on the second column
        similarity_scores.append(data[1].count(data[0][i]))

    # multiply the two numbers
    similarity_scores = [x * y for x, y in zip(data[0], similarity_scores)]

    return sum(similarity_scores)


# Part 2
print("Part 2")
print("----------------")
print("Test: " + str(calculate_similarity("Test.txt")))
print("Puzzle: " + str(calculate_similarity("Puzzle.txt")))
