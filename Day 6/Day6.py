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
        for j in range(len(data[i])):
            if data[i][j] == "^":
                coordinates = (i, j)
                direction = "up"
                return coordinates, direction
            elif data[i][j] == ">":
                coordinates = (i, j)
                direction = "right"
                return coordinates, direction
            elif data[i][j] == "v":
                coordinates = (i, j)
                direction = "down"
                return coordinates, direction
            elif data[i][j] == "<":
                coordinates = (i, j)
                direction = "left"
                return coordinates, direction


def count_locations(filename):
    completed_map = map_patrol_route(filename)

    # count amount of X's in the map
    count = 0
    for i in range(len(completed_map)):
        for j in range(len(completed_map[i])):
            if completed_map[i][j] == "X":
                count += 1

    return count

def map_patrol_route(filename):
    data = dataprep(filename)
    (x, y), direction = find_starting_position(data)
    repeating = False
    history = [(x, y), direction]
    temporary_counter = 0

    try:
        while True and not repeating and temporary_counter < 1000:
            data, x, y, direction, history = move_guard(data, x, y, direction, history)
            # repeating = check_for_loop(history)
            temporary_counter += 1

    except IndexError:
        for i in range(len(data)):
            print("".join(data[i]))
        print("\n")
        print("End of the map reached.")

    return data

def check_for_loop(history):

    # check if history has any duplicates
    for i in range(len(history)):
        for j in range(len(history)):
            # print(history[i], history[j])
            if i != j and history[i] == history[j]:
                print("Loop detected at", history[i])
                return True


def move_guard(data, x, y, direction, history):
    if x == 31 and y == 121 and direction == "left":
        print("Checkpoint reached")

    if direction == "up":

        # change every "." to "X" until you hit a "#"
        while data[x][y] != "#":
            if x < 0 or y < 0:
                raise IndexError

            data[x][y] = "X"
            x -= 1
            last_position = [(x, y), "up"]
            history.append(last_position)

        x += 1
        data[x][y] = ">"
        direction = "right"

    elif direction == "right":

        # change every "." to "X" until you hit a "#"
        while data[x][y] != "#":
            if x < 0 or y < 0:
                raise IndexError
            data[x][y] = "X"
            y += 1
            last_position = [(x, y), "right"]
            history.append(last_position)

        y -= 1
        data[x][y] = "v"
        direction = "down"

    elif direction == "down":

        # change every "." to "X" until you hit a "#"
        while data[x][y] != "#":
            if x < 0 or y < 0:
                raise IndexError
            data[x][y] = "X"
            x += 1
            last_position = [(x, y), "down"]
            history.append(last_position)

        data[x-1][y] = "<"
        direction = "left"
        x -= 1

    elif direction == "left":

        # change every "." to "X" until you hit a "#"
        while data[x][y] != "#":
            if x < 0 or y < 0:
                raise IndexError
            data[x][y] = "X"
            y -= 1
            last_position = [(x, y), "left"]
            history.append(last_position)

        data[x][y+1] = "^"
        direction = "up"
        y += 1

    return data, x, y, direction, history


# print(count_locations("Test.txt"))
# print(count_locations("Puzzle.txt"))
print(count_locations("Puzzle.txt"))
