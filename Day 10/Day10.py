def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    data = readfile(filename)
    data = data.split("\n")

    for i in range(len(data)):
        data[i] = list(data[i])

    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

    return data


def find_trailheads(data):
    trailheads = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                trailheads.append((i, j))

    return trailheads


# this function gets called by the main function for each trailhead
def determine_trailhead_score(data, start_position):
    score = 0
    rating = 0

    positions_to_check = [start_position]
    positions_already_added = [start_position]
    amount_of_positions_checked = [0]

    counter = 0
    checking = True

    while checking:
        temporary_positions = []

        for position in positions_to_check:
            x = position[0]
            y = position[1]

            if x < len(data[0]) - 1 and data[x+1][y] - data[x][y] == 1:
                temporary_positions.append((x+1, y))
                positions_already_added.append((x+1, y))

                if data[x+1][y] == 9:
                    rating += 1

            if x != 0 and data[x-1][y] - data[x][y] == 1:
                temporary_positions.append((x - 1, y))
                positions_already_added.append((x - 1, y))

                if data[x-1][y] == 9:
                    rating += 1

            if y < len(data) - 1 and data[x][y+1] - data[x][y] == 1:
                temporary_positions.append((x, y+1))
                positions_already_added.append((x, y+1))

                if data[x][y+1] == 9:
                    rating += 1

            if y != 0 and data[x][y-1] - data[x][y] == 1:
                temporary_positions.append((x, y-1))
                positions_already_added.append((x, y-1))

                if data[x][y-1] == 9:
                    rating += 1

        positions_to_check = temporary_positions

        amount_of_positions_checked.append(amount_of_positions_checked[-1] + len(positions_to_check))
        counter += 1

        if amount_of_positions_checked[counter] == amount_of_positions_checked[counter - 1]:
            checking = False

    double_positions = []
    for position in positions_already_added:
        if data[position[0]][position[1]] == 9 and position not in double_positions:
            score += 1
            double_positions.append(position)

    return score, rating

def calculate_total_trailhead_score(filename):
    data = dataprep(filename)
    trailheads = find_trailheads(data)

    scores = []

    for trailhead in trailheads:
        scores.append(determine_trailhead_score(data, trailhead)[0])

    return sum(scores), scores

# Part 1
# print(calculate_total_trailhead_score("Test.txt"))
# print(calculate_total_trailhead_score("Puzzle.txt"))

def calculate_total_trailhead_rating(filename):
    data = dataprep(filename)
    trailheads = find_trailheads(data)

    rating = []

    for trailhead in trailheads:
        rating.append(determine_trailhead_score(data, trailhead)[1])

    return sum(rating), rating


# Part 2
# print(calculate_total_trailhead_rating("Test.txt"))
print(calculate_total_trailhead_rating("Puzzle.txt"))