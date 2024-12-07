def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    my_file = readfile(filename)
    data = my_file.split("\n")
    data = [list(i) for i in data]

    return data


def find_starting_position(data):
    for i in range(len(data)):
        if "^" in data[i]:
            coordinates = (i, data[i].index("^"))
            direction = "up"
            return coordinates, direction

        elif "v" in data[i]:
            coordinates = (i, data[i].index("v"))
            direction = "down"
            return coordinates, direction

        elif "<" in data[i]:
            coordinates = (i, data[i].index("<"))
            direction = "left"
            return coordinates, direction

        elif ">" in data[i]:
            coordinates = (i, data[i].index(">"))
            direction = "right"
            return coordinates, direction
    else:
        print("No starting position found")


def count_locations(filename, send_data=False):
    data = dataprep(filename)
    completed_map = map_patrol_route(data)

    # count amount of X's in the map
    count = 0
    for i in range(len(completed_map[0])):
        for j in range(len(completed_map[0][i])):
            if completed_map[0][i][j] == "X":
                count += 1

    if send_data:
        # change the original starting position back to the original direction
        notation = "^"
        if completed_map[3] == "up":
            notation = "^"
        elif completed_map[3] == "down":
            notation = "v"
        elif completed_map[3] == "left":
            notation = "<"
        elif completed_map[3] == "right":
            notation = ">"

        completed_map[0][completed_map[2][0]][completed_map[2][1]] = notation

        return count, completed_map[0]
    else:
        return count


def map_patrol_route(data):
    start_position, start_direction = find_starting_position(data)
    (x, y) = start_position
    direction = start_direction
    history = []

    try:
        while 0 <= x < len(data) and 0 <= y < len(data[0]):
            data, x, y, direction, history, loop_detected = move_guard(data, x, y, direction, history)
            if loop_detected:
                return data, loop_detected, start_position, start_direction

    except IndexError:
        return data, False, start_position, start_direction


def check_for_loop(current_position, history, counter):
    counter += 1
    # only check every 500 steps
    if counter % 500 == 0:
        return False

    # check if current position has been visited before
    if history.count(current_position) > 0:
        return True


def move_guard(data, x, y, direction, history):
    loop_detected = False
    counter = 0

    if direction == "up":
        # change every "." to "X" until you hit a "#"

        while data[x][y] != "#" and data[x][y] != "0" or x < 0 or y < 0:
            if x < 0 or y < 0:
                raise IndexError
            data[x][y] = "X"
            x -= 1

        x += 1
        data[x][y] = ">"
        direction = "right"

    elif direction == "right":
        # change every "." to "X" until you hit a "#"
        while data[x][y] != "#" and data[x][y] != "0" or x < 0 or y < 0:
            if x < 0 or y < 0:
                raise IndexError
            data[x][y] = "X"
            y += 1

        y -= 1
        data[x][y] = "v"
        direction = "down"

    elif direction == "down":
        # change every "." to "X" until you hit a "#"
        while data[x][y] != "#" and data[x][y] != "0" or x < 0 or y < 0:
            if x < 0 or y < 0:
                print("end of map")
                raise IndexError
            data[x][y] = "X"
            x += 1

        data[x - 1][y] = "<"
        direction = "left"
        x -= 1

    elif direction == "left":
        # change every "." to "X" until you hit a "#"
        while data[x][y] != "#" and data[x][y] != "0" or x < 0 or y < 0:
            if x < 0 or y < 0:
                raise IndexError
            data[x][y] = "X"
            y -= 1

        data[x][y + 1] = "^"
        direction = "up"
        y += 1

    last_position = [(x, y), direction]
    if check_for_loop(last_position, history, counter):
        loop_detected = True
    history.append(last_position)

    return data, x, y, direction, history, loop_detected


# Part 1
# print(count_locations("Test.txt"))
# print(count_locations("Puzzle.txt"))


def find_creatable_loops(filename):
    data = dataprep(filename)
    loop_counter = 0

    # get coordinates of all walked positions in an unaltered map
    locations_amount, unaltered_locations = count_locations(filename, send_data=True)

    # place one obstacle at a time in each position (except the starting position) and see if it creates a loop
    for i in range(len(data)):
        for j in range(len(data[i])):
            if unaltered_locations[i][j] == "X" and not data[i][j] == "^" and not data[i][j] == ">" and not data[i][j] == "v" and not data[i][j] == "<":

                # print(f"Checking position {i}, {j}")
                # create a copy of the data
                new_data = [k.copy() for k in data]
                new_data[i][j] = "0"
                new_map_completed = map_patrol_route(new_data)

                if new_map_completed[1]:
                    loop_counter += 1
                    print(f"Loop detected at position {i}, {j}")
                    continue

    print("\n")
    print(f"Amount of loops detected: {loop_counter}")


# Part 2
# find_creatable_loops("Test.txt")
find_creatable_loops("Puzzle.txt")
