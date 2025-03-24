# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start amd end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    '''Checks that users enter the full word or the first letter of a word from a list of valid responses.'''

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter.
            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_answers}")


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


# Main routine goes here

make_statement("Fund Raising Calculator", "💰")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("Program Continues")