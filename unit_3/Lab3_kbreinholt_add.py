"""
Challenge: Import the file from project 1, do not copy and paste it.
Append 5 more items to the list.  Print the result.
"""

import Lab3_kbreinholt_list  as file
import functions as function
end_append = False
quit_list = ('q', 'Q', 'quit', 'Quit', 'QUIT')
print("Append items to your List (Q to quit): ")
while not end_append:
        input_string = input("Item: ")
        if input_string in quit_list:
                end_append = True
        else:
                file.camping_items.append(input_string)
function.print_statement(file.camping_items)



