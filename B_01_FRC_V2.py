import pandas
from tabulate import tabulate
from datetime import date
import math


# functions go here.
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start amd end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def yes_no_check(question):
    """checks that users enter a yes/y and a no/n"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Sorry, this is a yes(y) and no(n) question. Please answer with the 2 options.\n")


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''

The Program Will Ask You For...

    - The Name of the product you are selling
    - How many you plan on selling
    - The costs for each component of the product
    (variable expenses)
    - Whether or not you have fixed expenses (if you have
    fixed expenses, it will ask you what they are)
    - How much money you want to make (ie; your profit goal)
    - How much the recommended sales price should be rounded to.

The program outputs an itemised list of the variable and fixed
expenses (which includes the subtotals for these expenses)

Finally it will tell you how much you should sell each item
for you to reach your profit goal

The data will be written to a text file which has the same name
as your product and today's date.
    ''')


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


def get_expenses(exp_type, how_many=1):
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
    amount = how_many  # defaults to 1
    how_much_question = "How Much? $"

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
        if exp_type == "variable":

            amount = num_check(f"How many? <enter for {how_many}>: ", "integer", "")

            # Allow users to push <enter> to default to number of items being made.
            if amount == "":
                amount = how_many

            how_much_question = "Price for one? $"

        # get price for item (question customised depending on expense type).
        price_for_one = num_check(how_much_question, "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(price_for_one)

    # Make panda frame
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate row cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # apply currency formatting to currency columns.
    add_dollars = ['Amount', '$ / Item', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    # make expense frame into a string with the desired columns
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys', tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys', tablefmt='psql', showindex=False)

    # return all items for now so we can check loop.
    return expense_string, subtotal


def currency(x):
    return "${:.2f}".format(x)


def profit_goal(total_costs):
    """Calculates profit goal, Works out profit goal and total sales required"""
    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        response = input("What is your profit goal? (eg: $500 or 50%): ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]
            print("the percent amount is ", amount)

        else:
            # set response to amount for now.
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no_check(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars? , y / n ")
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no_check(f"Do you mean {amount}%? , y / n: ")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# rounding function
def round_up(amount, round_val):
    """Rounds amount to desired whole number"""
    return int(math.ceil(amount / round_val)) * round_val


# Main Routine goes here

# initialise variables

# assume we have no fixed variables
fixed_subtotal = 0
fixed_panda_string = ""

print(make_statement("Fund Raising Calculator", "💰"))

print()
want_instructions = yes_no_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

product_name = not_blank("Product Name: ")
quantity_made = num_check("Quantity being made: ", "integer")

print("Let's get our variable expenses...")
variable_expenses = get_expenses("variable", quantity_made)

variable_panda_string = variable_expenses[0]
variable_subtotal = variable_expenses[1]

# ask user if they have fixed expenses and retrieve them.
print()
has_fixed = yes_no_check("Do you have expenses? ")

if has_fixed == "yes":
    fixed_expenses = get_expenses("fixed")

    fixed_panda_string = fixed_expenses[0]
    fixed_subtotal = fixed_expenses[1]

if fixed_subtotal == 0:
    has_fixed = "no"
    fixed_panda_string = ""

total_expenses = variable_subtotal + fixed_subtotal
total_expenses_string = f"Total Expenses: ${total_expenses}"

# get profit goal here
target = profit_goal(total_expenses)
sales_target = total_expenses + target

# Calculate minimum selling price and round
# It to the nearest desired dollar amount
selling_price = (total_expenses + target) / quantity_made
round_to = num_check("Round To: ", 'integer')
suggested_price = round_up(selling_price, round_to)

# strings / output area

# **** Get current date for heading and filename ****
today = date.today()

# get day, month & year in separate strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Headings / Strings...
main_heading_string = make_statement(f"Fund Raising Calculator ({product_name}, {day}/{month})/{year}", "=")
quantity_string = f"Quantity being made: {quantity_made}"
variable_heading_string = make_statement("Variable Expenses", "-")
variable_subtotal_string = f"Variable Expenses Subtotal: ${variable_subtotal:.2f}"

# set up strings if we have fixed costs
if has_fixed == "yes":
    fixed_heading_string = make_statement("Fixed Expenses", "-")
    fixed_subtotal_string = f"Fixed Expenses Subtotal: ${fixed_subtotal:.2f}"

else:
    fixed_heading_string = make_statement("You have no fixed expenses.", "-")
    fixed_subtotal_string = f"Fixed Expenses Subtotal: $0.00"

selling_price_heading = make_statement("Selling Price Calculations", "-")
profit_goal_string = f"Profit Goal: ${target:.2f}"
sales_target_string = f"\nTotal Sales Needed: ${sales_target:.2f}"

minimum_price_string = f"Minimum Selling Price: ${selling_price:.2f}"
suggested_price_string = make_statement(f"Suggested Selling Price: ${suggested_price:.2f}", "*")

# list of strings to be outputted / written to file
to_write = [main_heading_string, quantity_string,
            "\n", variable_heading_string, variable_panda_string,
            variable_subtotal_string,
            "\n", fixed_heading_string, fixed_panda_string,
            fixed_subtotal_string, "\n",
            selling_price_heading, total_expenses_string,
            profit_goal_string, sales_target_string,
            minimum_price_string, "\n", suggested_price_string]

# print area
print()

for item in to_write:
    print(item)

# create file to hold data
file_name = f"{product_name}_{day}_{month}_{year}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
