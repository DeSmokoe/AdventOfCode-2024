def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    my_file = readfile(filename)
    data = my_file.split("\n")

    return data


def find_all_of_letter(data, letter):

    letter_coordinates = []

    # find every instance of the given letter in the data
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == letter:
                letter_coordinates.append([i, j])

    return letter_coordinates

def search_XMAS(filename):
    data = dataprep(filename)

    count = 0
    x_coordinates = find_all_of_letter(data, "X")

    # look for "M" around each "X" in each direction
    for i in range(len(x_coordinates)):
        x = x_coordinates[i][0]
        y = x_coordinates[i][1]

        if x >= 3 and data[x - 1][y] == "M" and data[x-2][y] == "A" and data[x-3][y] == "S":
            count += 1
            # MAS found above X

        if x <= len(data[x]) - 4 and data[x + 1][y] == "M" and data[x+2][y] == "A" and data[x+3][y] == "S":
            count += 1
            # MAS found below X

        if y >= 3 and data[x][y - 1] == "M" and data[x][y-2] == "A" and data[x][y-3] == "S":
            count += 1
            # MAS found left of X

        if y <= len(data[y]) - 1 - 3 and data[x][y + 1] == "M" and data[x][y+2] == "A" and data[x][y+3] == "S":
            count += 1
            # MAS found right of X

        if x <= len(data[x]) - 1 - 3 and y <= len(data[y]) - 1 - 3 and data[x+1][y+1] == "M" and data[x+2][y+2] == "A" and data[x+3][y+3] == "S":
            count += 1
            # MAS found below right of X

        if x >= 3 and y >= 3 and data[x-1][y-1] == "M" and data[x-2][y-2] == "A" and data[x-3][y-3] == "S":
            count += 1
            # MAS found above left of X

        if x <= len(data[x]) - 1 - 3 and y >= 3 and data[x+1][y-1] == "M" and data[x+2][y-2] == "A" and data[x+3][y-3] == "S":
            count += 1
            # MAS found below left of X

        if x >= 3 and y <= len(data[y]) - 1 - 3 and data[x-1][y+1] == "M" and data[x-2][y+2] == "A" and data[x-3][y+3] == "S":
            count += 1
            # MAS found above right of X

    return count

# Part 1
# print(search_XMAS("Test.txt"))
# print(search_XMAS("Puzzle.txt"))


def search_X_MAS(filename):
    data = dataprep(filename)

    total_count = 0
    a_coordinates = find_all_of_letter(data, "A")

    # look for "M" around each "X" in each direction
    for i in range(len(a_coordinates)):
        individual_count = 0

        x = a_coordinates[i][0]
        y = a_coordinates[i][1]

        # A is not on the edge
        if 0 < x < len(data[y]) - 1 and 0 < y < len(data[y]) - 1:

            # Look for M  left above A and S right below A
            if data[x - 1][y - 1] == "M" and data[x + 1][y + 1] == "S":
                individual_count += 1

            # Look for M  right above A and S left below A
            if data[x - 1][y + 1] == "M" and data[x + 1][y - 1] == "S":
                individual_count += 1

            # Look for M left below A and S right above A
            if data[x + 1][y - 1] == "M" and data[x - 1][y + 1] == "S":
                individual_count += 1

            # Look for M right below A and S left above A
            if data[x + 1][y + 1] == "M" and data[x - 1][y - 1] == "S":
                individual_count += 1

        # A cross only requires 2 lines of M, A, and S
        if individual_count > 1:
            total_count += 1

    return total_count


# Part 2
print(search_X_MAS("Test.txt"))
print(search_X_MAS("Puzzle.txt"))
