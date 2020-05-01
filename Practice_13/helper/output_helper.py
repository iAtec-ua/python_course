# Function helps results look better

# Colorama is used for producing colored terminal text and cursor positioning
from colorama import Fore
# prettytable helps creating pretty tables
from prettytable import PrettyTable


# Create function to add some style to output
def pretty_print(table, columns):
    # Check if there is no results
    if not table and len(table) == 0:
        print(Fore.CYAN, "No results found", Fore.RESET)
        return

    # Create object using PrettyTable
    output_table = PrettyTable(columns)
    # Iterate object to create a table
    for row in table:
        row_data = []
        for cell in columns:
            row_data.append(row[cell.lower()])
        output_table.add_row(row_data)

    print(output_table)
