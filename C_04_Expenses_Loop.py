def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. \n")


def num_check(question, num_type="float"):
    """Checks users enter an integer / float that is more than zero"""

    # checks number typer (float or int) and adds specific error.
    if num_type == "float":
        error = "Please enter a number more than 0"
    else:
        error = "Please enter an integer more than 0"

    # question / response loop
    while True:

        try:
            # ask for response in either float or int.
            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

            # more than zero or error.
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # lists for panda
    all_items = []

    # expenses dictionary

    # loop to get expenses
    while True:
        item_name = not_blank("Item Name: ")

        if (exp_type == "variable" and item_name == "xxx") and len(all_items) == 0:
            print("Oops! - you have not entered anything. "
                  "You need at least 1 item.")
        elif item_name == "xxx":
            break

        all_items.append(item_name)

    return all_items


# main routine starts here

# print("Getting variable costs... ")
# variable_expenses = get_expenses("variable")
# num_variable = len(variable_expenses)
# print(f"you have entered {num_variable} items")
# print()

print("Getting fixed costs... ")
fixed_expenses = get_expenses("fixed")
num_fixed = len(fixed_expenses)
print(f"you have entered {num_fixed} items")
print()