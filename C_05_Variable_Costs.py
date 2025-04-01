import pandas


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. \n")


def num_check(question, num_type="float", exit_code=None):
    """Checks users enter an integer / float that is more than zero"""

    # checks number typer (float or int) and adds specific error.
    if num_type == "float":
        error = "Please enter a number more than 0"
    else:
        error = "Please enter an integer more than 0"

    # question / response loop
    while True:

        response = input(question)

        # check exit code and return it if entered
        if response == exit_code:
            return response

        try:
            # ask for response in either float or int.
            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            # more than zero or error.
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type, how_many):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # lists for panda
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }

    # default amount to 1 for fixed expenses and
    # to avoid PEP 8 error for variable expenses
    amount = 1

    # loop to get expenses
    while True:

        # get item name and check it's not blank
        item_name = not_blank("Item Name: ")

        # check users enter at least one variable expense
        # NOTE: If you type the conditions without brackets,
        # All on one line and then add in enters
        # Pycharm will add in the brackets automatically.
        if (exp_type == "variable" and item_name == "xxx") and len(all_items) == 0:
            print("Oops! - you have not entered anything. "
                  "You need at least 1 item.")
            continue

        elif item_name == "xxx":
            break

        # Get item amount <enter> defaults to number of
        # products being made
        amount = num_check(f"How many? <enter for {how_many}>: ", "integer", "")

        if amount == "":
            amount = how_many

        cost = num_check("Price for one? ", "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(cost)

    # Make panda frame
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate row cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # return all items for now so we can check loop.
    return expense_frame, subtotal


# main routine starts here:

quantity_made = num_check("Quantity Being Made: ", "integer")
print()

print("Getting variable costs... ")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print(variable_panda)
print(variable_subtotal)
