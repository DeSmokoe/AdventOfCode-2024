def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    my_file = readfile(filename)
    data = my_file.split("\n")
    data = [list(i) for i in data]

    return data


def find_all_antenna_types(data):
    antenna_types = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != ".":
                current_antenna = data[i][j]
                antenna_types.append(current_antenna)

    return antenna_types


def find_antenna_locations(data):
    antenna_locations = []
    antenna_types = find_all_antenna_types(data)

    for antenna_type in antenna_types:
        current_antenna_locations = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == antenna_type:
                    current_antenna_locations.append((i, j))
        antenna_locations.append(current_antenna_locations)

    return antenna_types, antenna_locations


def create_duplicate_map(data):
    duplicate_map = []
    for i in range(len(data)):
        duplicate_map.append([])
        for j in range(len(data[i])):
            duplicate_map[i].append(data[i][j])

    return duplicate_map


def create_antinodes(filename, resonant_frequency=False):
    data = dataprep(filename)
    antenna_types, antenna_locations = find_antenna_locations(data)
    antinode_count = 0
    duplicate_map = create_duplicate_map(data)
    antenna_location = (0, 0)

    for antenna_type in antenna_types:
        antenna_counter = 0

        for antenna_location in antenna_locations[antenna_types.index(antenna_type)]:
            antenna_counter += 1

            if resonant_frequency:
                duplicate_map[antenna_location[0]][antenna_location[1]] = "#"  # mark the antenna on the map

            # check distance to all other antennas of the same type while ignoring the current antenna and all previous antennas
            for other_antenna_location in antenna_locations[antenna_types.index(antenna_type)][antenna_counter:]:

                distance = [(antenna_location[0] - other_antenna_location[0]),
                            (antenna_location[1] - other_antenna_location[1])]
                node1_in_map = True
                node2_in_map = True

                antinode1 = (antenna_location[0] + distance[0], antenna_location[1] + distance[1])
                antinode2 = (other_antenna_location[0] - distance[0], other_antenna_location[1] - distance[1])

                while node1_in_map or node2_in_map:
                    # draw 2 antinodes in a straight line behind both antennas with the same distance as they are from each other

                    if not resonant_frequency:
                        node1_in_map = False
                        node2_in_map = False

                    # check if antinode1 is within the map
                    if 0 <= antinode1[0] < len(data) and 0 <= antinode1[1] < len(data[0]):
                        if duplicate_map[antinode1[0]][antinode1[1]] != "#":
                            duplicate_map[antinode1[0]][antinode1[1]] = "#"
                        new_antinode1 = (antinode1[0] + distance[0], antinode1[1] + distance[1])
                        antinode1 = new_antinode1
                    else:
                        node1_in_map = False

                    # check if antinode2 is within the map
                    if 0 <= antinode2[0] < len(data) and 0 <= antinode2[1] < len(data[0]):
                        if duplicate_map[antinode2[0]][antinode2[1]] != "#":
                            duplicate_map[antinode2[0]][antinode2[1]] = "#"
                        new_antinode2 = (antinode2[0] - distance[0], antinode2[1] - distance[1])
                        antinode2 = new_antinode2
                    else:
                        node2_in_map = False

    for i in range(len(duplicate_map)):
        for j in range(len(duplicate_map[i])):
            if duplicate_map[i][j] == "#":
                antinode_count += 1

    return antinode_count

# Part 1
# print(create_antinodes("Test.txt"))
# print(create_antinodes("Puzzle.txt"))

# Part 2
# print(create_antinodes("Test.txt", True))
print(create_antinodes("Puzzle.txt", True))