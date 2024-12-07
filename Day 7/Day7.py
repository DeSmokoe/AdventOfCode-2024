def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    my_file = readfile(filename)
    data = my_file.split("\n")

    # remove every ":" from the data
    data = [i.replace(":", "") for i in data]

    # split the data for every space
    data = [i.split(" ") for i in data]

    # change all the numbers in the data to integers
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

    solution_list = []
    equation_list = []

    for i in range(len(data)):
        solution_list.append(data[i][0])
        equation_list.append(data[i][1:])

    return solution_list, equation_list


def evaluate_equations(filename, part2=False):
    solution_list, equation_list = dataprep(filename)
    solvable_solutions = []

    for equation in equation_list:
        current_solution = solution_list[equation_list.index(equation)]
        print("current solution: ", current_solution)

        results = {equation[0]}
        element_counter = 1

        for element in equation[1:]:
            element_counter += 1
            new_results = set()
            for result in results:
                new_results.add(result + int(element))
                new_results.add(result * int(element))
                if part2:
                    new_results.add(result * 10 ** len(str(element)) + int(element))
                results = new_results

            if element_counter == len(equation) and current_solution in results:
                solvable_solutions.append(current_solution)
                print("solvable solution: ", current_solution)
                break

    return sum(solvable_solutions)


# Part 1
# print("The sum of the solvable solutions is: ", evaluate_equations("Test.txt"))
#print("The sum of the solvable solutions is: ", evaluate_equations("Puzzle.txt"))
# print("The sum is: ", evaluate_equations("Personal.txt"))

# Part 2
# print(evaluate_equations("Test.txt", True))
print(evaluate_equations("Puzzle.txt", True))
