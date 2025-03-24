# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start amd end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


# Main Routine goes here
make_statement("Instructions", "ℹ️")
