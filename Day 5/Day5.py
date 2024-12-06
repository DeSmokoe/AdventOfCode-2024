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


# check if the given update has any pages in the wrong order
def find_wrong_order(update, ordering_rules, advanced=False):
    changed = False
    done = False

    while not done:
        change_counter = 0
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
                                    if advanced:
                                        # switch the order of the pages and continue checking
                                        update[update.index(rule[1])], update[update.index(page)] = update[update.index(page)], update[update.index(rule[1])]
                                        changed = True
                                        change_counter += 1
                                        continue
                                    else:
                                        return True
                        elif i == 1:
                            if rule[0] in update:
                                if update.index(rule[0]) > update.index(page):
                                    if advanced:
                                        # switch the order of the pages and continue checking
                                        update[update.index(rule[0])], update[update.index(page)] = update[update.index(page)], update[update.index(rule[0])]
                                        changed = True
                                        change_counter += 1
                                        continue
                                    else:
                                        return True
        if change_counter == 0:
            done = True

    return changed


# find the production updates that are in the correct order
def find_updates_correct_order(filename, originally_incorrect=False):
    ordering_rules, production_updates = dataprep(filename)
    correct_production_updates = []
    incorrect_production_updates = []

    for update in production_updates:
        if find_wrong_order(update, ordering_rules, originally_incorrect):
            incorrect_production_updates.append(update)
            continue

    # remove incorrect updates from the list of updates
    for update in production_updates:
        if update not in incorrect_production_updates:
            correct_production_updates.append(update)

    if originally_incorrect:
        return incorrect_production_updates
    else:
        return correct_production_updates


# find the middle number of each correct production update and return the sum
def calculate_sum_middle_numbers(filename, originally_incorrect=False):
    subset_production_updates = find_updates_correct_order(filename, originally_incorrect)
    middle_numbers = []

    for update in subset_production_updates:
        middle_numbers.append(int(update[len(update) // 2]))

    return sum(middle_numbers)


# Part 1
# print(calculate_sum_middle_numbers("Test.txt"))
# print(calculate_sum_middle_numbers("Puzzle.txt"))

# Part 2
print(calculate_sum_middle_numbers("Test.txt", True))
print(calculate_sum_middle_numbers("Puzzle.txt", True))
