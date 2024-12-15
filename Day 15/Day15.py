def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    data = readfile(filename)
    data = data.split(" ")
    found = False

    warehouse_map = []
    instructions = []

    for i in range(len(data[0])):
        if not found:
            if data[0][i] == ">" or data[0][i] == "<" or data[0][i] == "^" or data[0][i] == "v":
                found = True
                warehouse_map = data[0][:i]
                instructions.append(data[0][i])
        elif found:
            instructions.append(data[0][i])

    # remove all new lines in instructions
    instructions = [x.replace("\n", "") for x in instructions]

    # turn warehouse_map into a list of lists
    warehouse_map = [list(x) for x in warehouse_map.split("\n")]

    # remove all empty strings from warehouse_map
    warehouse_map = [x for x in warehouse_map if x != []]

    return warehouse_map, instructions


def find_robot_pos(warehouse_map):
    # find the starting position of the robot
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[i])):
            if warehouse_map[i][j] == "@":
                robot_pos = (i, j)
                return robot_pos


def move_robot(warehouse_map, instruction):
    x, y = find_robot_pos(warehouse_map)
    box_placed = False

    if instruction == "^":
        if warehouse_map[x-1][y] == "#": # if there is a wall in front of the robot
            return warehouse_map
        elif warehouse_map[x-1][y] == "O": # if there is a box in front of the robot
            if can_box_move(warehouse_map, "^", x-1, y):

                # check all following coordinates until we find a free space
                while not box_placed:
                    if warehouse_map[x-1][y] == "O":
                        x -= 1
                    elif warehouse_map[x - 1][y] == ".":
                        warehouse_map[x - 1][y] = "O"
                        box_placed = True

                x, y = find_robot_pos(warehouse_map)
                warehouse_map[x - 1][y] = "@"
                warehouse_map[x][y] = "."
                return warehouse_map


            else:
                return warehouse_map

        else:   # if there is a free space in front of the robot
            warehouse_map[x-1][y] = "@"
            warehouse_map[x][y] = "."

    if instruction == "v":
        if warehouse_map[x+1][y] == "#": # if there is a wall in front of the robot
            return warehouse_map
        elif warehouse_map[x+1][y] == "O": # if there is a box in front of the robot
            if can_box_move(warehouse_map, "v", x+1, y):

                # check all following coordinates until we find a free space
                while not box_placed:
                    if warehouse_map[x+1][y] == "O":
                        x += 1
                    elif warehouse_map[x+1][y] == ".":
                        warehouse_map[x+1][y] = "O"
                        box_placed = True

                x, y = find_robot_pos(warehouse_map)
                warehouse_map[x+1][y] = "@"
                warehouse_map[x][y] = "."
                return warehouse_map

            else:
                return warehouse_map

        else:   # if there is a free space in front of the robot
            warehouse_map[x+1][y] = "@"
            warehouse_map[x][y] = "."

    if instruction == "<":
        if warehouse_map[x][y-1] == "#": # if there is a wall in front of the robot
            return warehouse_map
        elif warehouse_map[x][y-1] == "O": # if there is a box in front of the robot
            if can_box_move(warehouse_map, "<", x, y-1):

                # check all following coordinates until we find a free space
                while not box_placed:
                    if warehouse_map[x][y - 1] == "O":
                        y -= 1
                    elif warehouse_map[x][y - 1] == ".":
                        warehouse_map[x][y - 1] = "O"
                        box_placed = True

                x, y = find_robot_pos(warehouse_map)
                warehouse_map[x][y - 1] = "@"
                warehouse_map[x][y] = "."
                return warehouse_map
            else:
                return warehouse_map

        else:   # if there is a free space in front of the robot
            warehouse_map[x][y-1] = "@"
            warehouse_map[x][y] = "."

    if instruction == ">":
        if warehouse_map[x][y+1] == "#": # if there is a wall in front of the robot
            return warehouse_map
        elif warehouse_map[x][y+1] == "O": # if there is a box in front of the robot
            if can_box_move(warehouse_map, ">", x, y+1):

                # check all following coordinates until we find a free space
                while not box_placed:
                    if warehouse_map[x][y+1] == "O":
                        y += 1
                    elif warehouse_map[x][y+1] == ".":
                        warehouse_map[x][y+1] = "O"
                        box_placed = True

                x, y = find_robot_pos(warehouse_map)
                warehouse_map[x][y+1] = "@"
                warehouse_map[x][y] = "."
                return warehouse_map

            else:
                return warehouse_map

        else:   # if there is a free space in front of the robot
            warehouse_map[x][y+1] = "@"
            warehouse_map[x][y] = "."

    return warehouse_map


def can_box_move(warehouse_map, direction, x, y):

    if direction == "^":
        if warehouse_map[x-1][y] == "#":
            return False
        elif warehouse_map[x-1][y] == "O":
            return can_box_move(warehouse_map, direction, x-1, y)
        elif warehouse_map[x-1][y] == ".":
            return True

    elif direction == "v":
        if warehouse_map[x+1][y] == "#":
            return False
        elif warehouse_map[x+1][y] == "O":
            return can_box_move(warehouse_map, direction, x+1, y)
        elif warehouse_map[x+1][y] == ".":
            return True

    elif direction == "<":
        if warehouse_map[x][y-1] == "#":
            return False
        elif warehouse_map[x][y-1] == "O":
            return can_box_move(warehouse_map, direction, x, y-1)
        elif warehouse_map[x][y-1] == ".":
            return True

    elif direction == ">":
        if warehouse_map[x][y+1] == "#":
            return False
        elif warehouse_map[x][y+1] == "O":
            return can_box_move(warehouse_map, direction, x, y+1)
        elif warehouse_map[x][y+1] == ".":
            return True


def calculate_sum_GPS(warehouse_map):
    # calculate the sum of GPS coordinates of all the boxes
    total_sum = 0

    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[i])):
            if warehouse_map[i][j] == "O":
                total_sum += i*100 + j

    return total_sum


def run(filename):
    warehouse_map, instructions = dataprep(filename)

    for instruction in instructions:
        warehouse_map = move_robot(warehouse_map, instruction)

    score = calculate_sum_GPS(warehouse_map)

    return score


# print(run("Test2.txt"))    # smaller example map
# print(run("Test.txt"))    # larger example map
# print(run("Puzzle.txt"))    # Puzzle input

