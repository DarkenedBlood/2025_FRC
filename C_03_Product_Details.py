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


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. \n")


# Main routine goes here.
while True:
    product_name = not_blank("Product Name: ")
    quantity_made = num_check("Quantity being made: ", "integer")

    if quantity_made == 1:
        print(f"you are making 1 {product_name}")
        print()
    else:
        print(f"you are making {quantity_made} {product_name}s")
        print()


