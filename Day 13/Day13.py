from math import isclose

def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    data = readfile(filename)
    data = data.split("\n\n")
    data = [x.replace("\n", " ") for x in data]
    new_data = [0] * len(data)
    A_instructions = []
    B_instructions = []
    prize = []

    for i in range(len(data)):
        new_data[i] = data[i].split(" ")

    for i in range(len(new_data)):
            A_instructions.append((int(new_data[i][2][2:-1]), int(new_data[i][3][2:])))
            B_instructions.append((int(new_data[i][6][2:-1]), int(new_data[i][7][2:])))
            prize.append((int(new_data[i][9][2:-1]), int(new_data[i][10][2:])))

    return A_instructions, B_instructions, prize


def solve_equation_brute_force(A, B, prize):

    for k in range(100):
        for l in range(100):
            if (A[0] * k + B[0] * l == prize[0]) and (A[1] * k + B[1] * l == prize[1]):
                return k, l

    return 0, 0


def solve_equation(A, B, prize, part2=False):
    if part2:
        error = 10000000000000
    else:
        error = 0

    x1 = A[0]
    y1 = B[0]
    x2 = A[1]
    y2 = B[1]
    p1 = prize[0] + error
    p2 = prize[1] + error

    click_b = (p2 - (x2*p1/x1)) / (y2 - (x2*y1/x1))
    click_a = (p1 - (y1*click_b)) / x1

    if click_b < 0 or click_a < 0:
        return False

    if not part2:
        if int(click_a) >= 100 or int(click_b) >= 100:
            return False


    if part2:
        if isclose(click_a, round(click_a), rel_tol=1e-15) and isclose(click_b, round(click_b), rel_tol=1e-15):
            return round(click_a), round(click_b)
    else:
        if isclose(click_a, round(click_a)) and isclose(click_b, round(click_b)):
            return round(click_a), round(click_b)


def run(filename, part2=False):
    A_instructions, B_instructions, prize = dataprep(filename)

    clicks_a = 0
    clicks_b = 0

    for i in range(len(prize)):
        clicks = solve_equation(A_instructions[i], B_instructions[i], prize[i], part2)
        if clicks:
            clicks_a += clicks[0]
            clicks_b += clicks[1]

    tokens = clicks_a * 3 + clicks_b

    return tokens

# print(run("Test.txt"))
# print(run("Puzzle.txt"))

# Part 2
print(run("Puzzle.txt", True))