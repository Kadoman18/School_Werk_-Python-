"""
Challenge: Import the file from project 3, do not copy and paste it.
You don’t have binoculars. So, remove that object from the camping list. Print the result.
"""
'''
Again, Trying to do this as fun and complex as I can to challenge myself so I am importing from project 1.
I will remove 'Lamp'
'''
import Lab3_kbreinholt_list as file
import functions as function
file.camping_items.remove('Lamp')
function.print_statement(file.camping_items)