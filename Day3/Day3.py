def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    my_file = readfile(filename)
    data = my_file

    return data


def find_digits(data, digit_number):
    numbers = []

    if not data[0].isdigit():
        return False

    for i in range(len(data)):
        if data[i].isdigit():
            numbers.append(data[i])
        elif digit_number == 1 and data[i] == ",":
            return numbers
        elif digit_number == 2 and data[i] == ")":
            return numbers
        else:
            return False
    return numbers

def determine_instructions(data):
    i = 0
    potential_digits = data[i:i + 3]

    if find_digits(potential_digits, 1):
        first_digit = find_digits(potential_digits, 1)
        i += len(first_digit)
        if data[i] == ",":
            i += 1
            potential_digits = data[i:i + 3]
            if find_digits(potential_digits, 2):
                second_digit = find_digits(potential_digits, 2)
                i += len(second_digit)
                if data[i] == ")":
                    first_digit = int("".join(first_digit))
                    second_digit = int("".join(second_digit))
                    return first_digit, second_digit

def find_instructions(data):
    data = dataprep(data)

    # find instructions that follow the structure of "mul(x, y)" whereby x and y are 1-3 digit numbers

    instructions = []

    for i in range(len(data)):
        if data[i] == "m" and data[i+1] == "u" and data[i+2] == "l" and data[i+3] == "(":
            i += 4
            shortened_data = data[i:i + 9]
            if determine_instructions(shortened_data):
                instructions.append(determine_instructions(shortened_data))

    return instructions

def calculate_instructions(instructions):

    # multiply the two numbers
    instructions = [x * y for x, y in instructions]
    return sum(instructions)


# Part 1
print(calculate_instructions(find_instructions("Test.txt")))
print(calculate_instructions(find_instructions("Puzzle.txt")))


def find_instructions_advanced(data):
    data = dataprep(data)
    enable = True
    instructions = []

    for i in range(len(data)):
        if data[i] == "m" and data[i+1] == "u" and data[i+2] == "l" and data[i+3] == "(" and enable:
            i += 4
            shortened_data = data[i:i+9]
            if determine_instructions(shortened_data):
                instructions.append(determine_instructions(shortened_data))

        if data[i] == "d" and data[i + 1] == "o" and data[i + 2] == "(" and data[i + 3] == ")":
            i += 4
            enable = True

        elif data[i] == "d" and data[i + 1] == "o" and data[i + 2] == "n" and data[i + 3] == "'" and data[i + 4] == "t" and data[i + 5] == "(":
            i += 6
            enable = False

    return instructions


# part 2
print(calculate_instructions(find_instructions_advanced("Test.txt")))
print(calculate_instructions(find_instructions_advanced("Puzzle.txt")))
