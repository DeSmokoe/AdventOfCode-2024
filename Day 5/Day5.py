def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(filename):
    my_file = readfile(filename)

    # split data at empty line
    data = my_file.split("\n\n")

    # prep first part of data into a list of 1*2 lists
    ordering_rules = data[0].split("\n")
    ordering_rules = [rule.split("|") for rule in ordering_rules]

    # prep second part of data into a list of 1*x lists (where x can be any whole number)
    production_pages = data[1].split("\n")
    production_pages = [page.split(",") for page in production_pages]

    return ordering_rules, production_pages


# find the production updates that are in the correct order
def find_updates_correct_order(filename):
    ordering_rules, production_updates = dataprep(filename)
    correct_production_updates = []
    incorrect_production_updates = []

    for update in production_updates:

        for page in update:

            # check if page appears in ordering rules
            for rule in ordering_rules:

                # find each instance of page in each rule
                for i in range(len(rule)):
                    if page == rule[i]:

                        # if page is found at the start of the rule, check if the accompanying page is found later
                        if i == 0:
                            if rule[1] in update:
                                if update.index(rule[1]) < update.index(page):
                                    incorrect_production_updates.append(update)
                                    break
                        elif i == 1:
                            if rule[0] in update:
                                if update.index(rule[0]) > update.index(page):
                                    incorrect_production_updates.append(update)
                                    break

    # remove incorrect updates from the list of updates
    for update in production_updates:
        if update not in incorrect_production_updates:
            correct_production_updates.append(update)

    return correct_production_updates


def calculate_sum_middle_numbers(filename):
    correct_production_updates = find_updates_correct_order(filename)
    middle_numbers = []

    for update in correct_production_updates:
        middle_numbers.append(int(update[len(update) // 2]))

    return sum(middle_numbers)


# Part 1
print(calculate_sum_middle_numbers("Test.txt"))
print(calculate_sum_middle_numbers("Puzzle.txt"))

