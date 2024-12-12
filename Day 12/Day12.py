def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    data = readfile(filename)
    data = data.split("\n")

    data = tuple(data)

    return data


def find_neighbours(data, position):
    x, y = position

    up = None
    down = None
    left = None
    right = None

    if x < len(data) - 1 and data[x][y] == data[x+1][y]:
        down = (x+1, y)
    if x > 0 and data[x][y] == data[x-1][y]:
        up = (x-1, y)
    if y < len(data[x]) - 1 and data[x][y] == data[x][y+1]:
        right = (x, y+1)
    if y > 0 and data[x][y] == data[x][y-1]:
        left = (x, y-1)

    return up, down, left, right


def has_neighbour(data, position, direction):

    up, down, left, right = find_neighbours(data, position)

    if direction == "up":
        if up is not None:
            return True
    elif direction == "down":
        if down is not None:
            return True
    elif direction == "left":
        if left is not None:
            return True
    elif direction == "right":
        if right is not None:
            return True

    return False


def find_unique_sides(data, position, up, down, left, right):
    sides = 0

    if up is None:    # top border
        if left is not None and right is not None:
            if has_neighbour(data, left, "up") and has_neighbour(data, right, "up"):
                sides += 1
            elif has_neighbour(data, left, "up") or has_neighbour(data, right, "up"):
                sides += 0.5
            else:
                sides += 0
        elif left is not None:
            if has_neighbour(data, left, "up"):
                sides += 1
            else:
                sides += 0.5
        elif right is not None:
            if has_neighbour(data, right, "up"):
                sides += 1
            else:
                sides += 0.5
        else:
            sides += 1

    if down is None:    # bottom border
        if left is not None and right is not None:
            if has_neighbour(data, left, "down") and has_neighbour(data, right, "down"):
                sides += 1
            elif has_neighbour(data, left, "down") or has_neighbour(data, right, "down"):
                sides += 0.5
            else:
                sides += 0
        elif left is not None:
            if has_neighbour(data, left, "down"):
                sides += 1
            else:
                sides += 0.5
        elif right is not None:
            if has_neighbour(data, right, "down"):
                sides += 1
            else:
                sides += 0.5
        else:
            sides += 1

    if left is None:    # left border
        if up is not None and down is not None:
            if has_neighbour(data, up, "left") and has_neighbour(data, down, "left"):
                sides += 1
            elif has_neighbour(data, up, "left") or has_neighbour(data, down, "left"):
                sides += 0.5
            else:
                sides += 0
        elif up is not None:
            if has_neighbour(data, up, "left"):
                sides += 1
            else:
                sides += 0.5
        elif down is not None:
            if has_neighbour(data, down, "left"):
                sides += 1
            else:
                sides += 0.5
        else:
            sides += 1

    if right is None:    # right border
        if up is not None and down is not None:
            if has_neighbour(data, up, "right") and has_neighbour(data, down, "right"):
                sides += 1
            elif has_neighbour(data, up, "right") or has_neighbour(data, down, "right"):
                sides += 0.5
            else:
                sides += 0
        elif up is not None:
            if has_neighbour(data, up, "right"):
                sides += 1
            else:
                sides += 0.5
        elif down is not None:
            if has_neighbour(data, down, "right"):
                sides += 1
            else:
                sides += 0.5
        else:
            sides += 1

    print(f"position: {position}, Sides: {sides}")

    return sides


def find_all_plots(data, position, area, perimeter, checked_positions, new_positions, unique_regions, area_list,
                   perimeter_list, sides):

    new_positions.append(position)
    checked_positions.add(position)
    up, down, left, right = find_neighbours(data, position)

    perimeter = 4
    area = 1
    sides = find_unique_sides(data, position, up, down, left, right)

    if up is not None:
        perimeter -= 1
    if down is not None:
        perimeter -= 1
    if left is not None:
        perimeter -= 1
    if right is not None:
        perimeter -= 1

    total_area = area
    total_perimeter = perimeter
    total_sides = sides

    for neighbour in [up, down, left, right]:
        if neighbour is not None and neighbour not in checked_positions:
            neighbour_area, neighbour_perimeter, neighbour_sides = find_all_plots(data, neighbour, area, perimeter,
                                                                                  checked_positions, new_positions,
                                                                                  unique_regions, area_list,
                                                                                  perimeter_list, sides)
            total_area += neighbour_area
            total_perimeter += neighbour_perimeter
            total_sides += neighbour_sides

    return total_area, total_perimeter, total_sides


def run(filename):
    data = dataprep(filename)
    total_price = 0
    total_price_discount = 0

    checked_positions = set()

    new_positions = []
    unique_regions = []

    area_list = []
    perimeter_list = []
    sides_list = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) in checked_positions:
                continue

            area = 0
            perimeter = 0
            sides = 0

            position = (i, j)

            area, perimeter, sides = find_all_plots(data, position, area, perimeter, checked_positions, new_positions,
                                                    unique_regions, area_list, perimeter_list, sides)

            # add new checked_positions to unique_regions in a new list
            unique_regions.append(new_positions.copy())
            area_list.append(area)
            perimeter_list.append(perimeter)
            sides_list.append(sides)

            new_positions.clear()

    print(f"Areas: {area_list}")
    print(f"Perimeters: {perimeter_list}")
    print(f"Sides: {sides_list}")
    print(unique_regions)

    for i in range(len(unique_regions)):
        total_price += area_list[i] * perimeter_list[i]

    for i in range(len(unique_regions)):
        total_price_discount += area_list[i] * sides_list[i]

    return total_price, total_price_discount


# print(run("Test.txt"))
# print(run("Test2.txt"))
# print(run("Test3.txt"))
# print(run("Test4.txt"))     # E & X regions only — price of 236 part 2 (17x12 + 4x4 + 4x4)
# print(run("Test5.txt"))   # A & B regions only — price of 368 part 2
# print(run("Test6.txt"))   # Personal — All A's

print(run("Puzzle.txt"))
