# Function helps results look better

# Colorama is used for producing colored terminal text and cursor positioning
from colorama import Fore
# prettytable helps creating pretty tables
from prettytable import PrettyTable


# Create function to add some style to output
def pretty_print(table):
    # Check if there is no results
    if not table or len(table) == 0:
        print(Fore.RED, "No results", Fore.RESET)

    print(Fore.GREEN, "Results:", Fore.RESET)

    # Create object using PrettyTable
    output_table = PrettyTable(table[0].keys())
    # Iterate object to create a table
    for row in table:
        output_table.add_row(list(row.values()))

    print(output_table)
