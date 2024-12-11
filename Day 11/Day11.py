from functools import cache


def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    data = readfile(filename)
    data = data.split(" ")

    # convert all elements to integers
    for i in range(len(data)):
        data[i] = int(data[i])

    return data

@cache
def update_stone(value):

    if value == 0:
        return 1, None

    elif len(str(value)) % 2 == 0:
        # split number in left half and right half
        left = str(value)[:len(str(value))//2]
        right = str(value)[len(str(value))//2:]

        return int(left), int(right)

    else:
        return value*2024, None

@cache
def blink_part2(stone, depth):
    left_stone, right_stone = update_stone(stone)

    if depth == 1:
        if right_stone is None:
            return 1
        else:
            return 2

    else:
        output = blink_part2(left_stone, depth - 1)
        if right_stone is not None:
            output += blink_part2(right_stone, depth - 1)

        return output


def run(filename, amount):
    data = dataprep(filename)
    output = 0

    for stone in data:
        print(f"Stone: {stone}")
        output += blink_part2(stone, amount)

    return output

# Part 1
# print(run("Test.txt", 25))
#print(run("Puzzle.txt", 25))


# Part 2
# print(run("Test2.txt", 25))
print(run("Puzzle.txt", 75))
