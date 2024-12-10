def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    data = readfile(filename)

    return data


def create_expanded_disk(filename):
    data = dataprep(filename)
    ID_number = 0
    free_space = False
    expanded_disk_map = []

    for i in range(len(data)):
        for j in range(int(data[i])):
            if not free_space:
                expanded_disk_map.append(ID_number)
            else:
                expanded_disk_map.append(".")

        if not free_space:
            ID_number += 1
        free_space = not free_space

    return expanded_disk_map


def sort_expanded_disk(filename):
    expanded_disk_map = create_expanded_disk(filename)

    for i in range(len(expanded_disk_map)):
        print("Current position: ", i)
        if expanded_disk_map[i] == ".":
            file_to_move = find_last_int_position(expanded_disk_map)

            if file_to_move < i:
                return expanded_disk_map

            expanded_disk_map[i] = expanded_disk_map[find_last_int_position(expanded_disk_map)]
            expanded_disk_map[file_to_move] = "."

    return expanded_disk_map


def find_last_int_position(disk_map):
    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i] != ".":
            return i


def calculate_checksum(filename, part2=False):
    if part2:
        sorted_disk = sort_expanded_disk_clusters(filename)
    else:
        sorted_disk = sort_expanded_disk(filename)
    checksum = 0

    for i in range(len(sorted_disk)):
        if sorted_disk[i] != "." and sorted_disk[i] != "X":
            checksum += i*sorted_disk[i]

    return checksum

# Part 1
# print(calculate_checksum("Test.txt"))
# print(calculate_checksum("Puzzle.txt"))


def sort_expanded_disk_clusters(filename):
    expanded_disk_map = create_expanded_disk(filename)
    unmovable_files = []

    for i in range(len(expanded_disk_map)):
        cluster_size = 0
        new_cluster = False
        print("Current position: ", i)

        if expanded_disk_map[i] == ".":
            cluster_size += 1
            k = 1
            while not new_cluster and i + k < len(expanded_disk_map):
                if expanded_disk_map[i+k] == ".":
                    k += 1
                    cluster_size += 1
                else:
                    new_cluster = True

            cluster_position_list, cluster_available = find_last_cluster_position(expanded_disk_map, cluster_size, i)

            if not cluster_available:
                i += cluster_size
            else:
                for n in range(len(cluster_position_list)):
                    if cluster_position_list[n] in unmovable_files:
                        break
                    expanded_disk_map[i + n] = expanded_disk_map[cluster_position_list[n]]
                    expanded_disk_map[cluster_position_list[n]] = "X"
                    unmovable_files.append(i+n)

    return expanded_disk_map

def find_last_cluster_position(disk_map, target_cluster_size, empty_space_position):
    position_list = []
    found_suitable_cluster = False
    cluster_available = True
    i = len(disk_map) - 1

    while not found_suitable_cluster and cluster_available:
        position_list = []

        while i > empty_space_position:
            if found_suitable_cluster:
                break
            elif disk_map[i] == "." or disk_map[i] == "X":
                i -= 1
            elif disk_map[i] != "." and disk_map[i] != "X":
                found_cluster_size = 1
                position_list.append(i)

                while True:
                    if i - 1 >= 0 and disk_map[i - 1] == disk_map[i]:
                        position_list.append(i - 1)
                        found_cluster_size += 1
                        i -= 1

                    elif disk_map[i - 1] != disk_map[i] or i - 1 < 0:

                        if found_cluster_size <= target_cluster_size:
                            found_suitable_cluster = True
                            break
                        else:
                            position_list = []
                            i -= 1
                            break

        if i <= empty_space_position and not found_suitable_cluster:
            cluster_available = False
            print("No suitable cluster found")

    return position_list, cluster_available


# Part 2
# print(calculate_checksum("Test.txt", True))
print(calculate_checksum("Puzzle.txt", True))
