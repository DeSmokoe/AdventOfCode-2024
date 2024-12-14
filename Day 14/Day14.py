def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    data = readfile(filename)
    data = data.split("\n")
    data = [i.split(" ") for i in data]

    positions = []
    velocities = []

    for i in range(len(data)):
        data[i][0] = data[i][0].replace("p=", "")
        data[i][1] = data[i][1].replace("v=", "")

        positions.append(data[i][0].split(","))
        velocities.append(data[i][1].split(","))

    # change velocity and position to integers
    for i in range(len(positions)):
        for j in range(len(positions[i])):
            positions[i][j] = int(positions[i][j])
            velocities[i][j] = int(velocities[i][j])

    return positions, velocities


def update_positions(positions, velocities, x_range, y_range):

    for i in range(len(positions)):
        for j in range(len(positions[i])):
            positions[i][j] += velocities[i][j]

            if j == 0 and positions[i][j] < 0:
                positions[i][j] = x_range + positions[i][j]
            elif j == 1 and positions[i][j] < 0:
                positions[i][j] = y_range + positions[i][j]

            if j == 0 and positions[i][j] >= x_range:
                positions[i][j] = positions[i][j] - x_range
            elif j == 1 and positions[i][j] >= y_range:
                positions[i][j] = positions[i][j] - y_range

    return positions

def calculate_safety_factor(positions, x_range, y_range):

    first_quadrant = []
    second_quadrant = []
    third_quadrant = []
    fourth_quadrant = []

    for i in range(len(positions)):
        if positions[i][0] < (x_range - 1)/2 and positions[i][1] < (y_range - 1)/2:
            first_quadrant.append(positions[i])
        elif positions[i][0] > (x_range - 1)/2 and positions[i][1] < (y_range - 1)/2:
            second_quadrant.append(positions[i])
        elif positions[i][0] < (x_range - 1)/2 and positions[i][1] > (y_range - 1)/2:
            third_quadrant.append(positions[i])
        elif positions[i][0] > (x_range - 1)/2 and positions[i][1] > (y_range - 1)/2:
            fourth_quadrant.append(positions[i])

    safety_score = len(first_quadrant) * len(second_quadrant) * len(third_quadrant) * len(fourth_quadrant)

    return safety_score

def draw_grid(positions, x_range, y_range):
    first_quadrant = []
    second_quadrant = []
    third_quadrant = []
    fourth_quadrant = []
    fifth_quadrant = []
    sixth_quadrant = []
    seventh_quadrant = []
    eighth_quadrant = []
    ninth_quadrant = []

    for i in range(len(positions)):
        if positions[i][0] < (x_range - 1)/3 and positions[i][1] < (y_range - 1)/3:
            first_quadrant.append(positions[i])
        elif positions[i][0] > (x_range - 1)/3 and positions[i][0] < 2*(x_range - 1)/3 and positions[i][1] < (y_range - 1)/3:
            second_quadrant.append(positions[i])
        elif positions[i][0] > 2*(x_range - 1)/3 and positions[i][1] < (y_range - 1)/3:
            third_quadrant.append(positions[i])
        elif positions[i][0] < (x_range - 1)/3 and positions[i][1] > (y_range - 1)/3 and positions[i][1] < 2*(y_range - 1)/3:
            fourth_quadrant.append(positions[i])
        elif positions[i][0] > (x_range - 1)/3 and positions[i][0] < 2*(x_range - 1)/3 and positions[i][1] > (y_range - 1)/3 and positions[i][1] < 2*(y_range - 1)/3:
            fifth_quadrant.append(positions[i])
        elif positions[i][0] > 2*(x_range - 1)/3 and positions[i][1] > (y_range - 1)/3 and positions[i][1] < 2*(y_range - 1)/3:
            sixth_quadrant.append(positions[i])
        elif positions[i][0] < (x_range - 1)/3 and positions[i][1] > 2*(y_range - 1)/3:
            seventh_quadrant.append(positions[i])
        elif positions[i][0] > (x_range - 1)/3 and positions[i][0] < 2*(x_range - 1)/3 and positions[i][1] > 2*(y_range - 1)/3:
            eighth_quadrant.append(positions[i])
        elif positions[i][0] > 2*(x_range - 1)/3 and positions[i][1] > 2*(y_range - 1)/3:
            ninth_quadrant.append(positions[i])

    if 4 * len(fifth_quadrant) >= len(first_quadrant) + len(second_quadrant) + len(third_quadrant) + len(fourth_quadrant) + len(sixth_quadrant) + len(seventh_quadrant) + len(eighth_quadrant) + len(ninth_quadrant):

        grid = [["." for i in range(x_range)] for j in range(y_range)]

        for i in range(len(positions)):
            grid[positions[i][1]][positions[i][0]] = "#"

        for i in range(len(grid)):
            print("".join(grid[i]))

    return


def run(filename):
    x_range = 101
    y_range = 103

    if filename == "Test.txt":
        x_range = 11
        y_range = 7


    positions, velocities = dataprep(filename)

    seconds = 7900

    while seconds > 0:
        positions = update_positions(positions, velocities, x_range, y_range)
        seconds -= 1

        print("Seconds: ", seconds)

        if seconds < 2900:
            draw_grid(positions, x_range, y_range)
            print("\n")

    safety_score = calculate_safety_factor(positions, x_range, y_range)


    return safety_score


# Part 1
# print(run("Test.txt"))
print(run("Puzzle.txt"))


