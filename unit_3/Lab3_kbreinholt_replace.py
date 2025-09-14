"""
Challenge: Import the file from project 2, do not copy and paste it.
Replace one of the string objects from the camping list with “binoculars”.
Print the result.
"""
'''
I know I should be importing project 2 but I am really trying to do this more
complicated and user friendly so I will import project 1, Please let me know if this is not Ok.
'''
import random as r
import functions as function
import Lab3_kbreinholt_list as file
index = r.randint(0, len(file.camping_items))
file.camping_items.remove(file.camping_items[index])
file.camping_items.insert(index, "Binoculars")
function.print_statement(file.camping_items)