'''
You are the owner of a restaurant. Ask one of your employees to write
a program which takes a total from a bill for dinner and prints out
suggestions for a 15% tip and 20% tip. Then gives the total for the meal
with the 15% tip and another with the 20% tip. Use F-strings.
'''

total = float(input())
tip15 = total * 0.15
tip20 = total * 0.2
print(f'Please choose a tip for todays Meal:'
      '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
      f'\n15%: ${tip15:.2f}            Total: ${(total + tip15):.2f}'
      '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
      f'\n20%: ${tip20:.2f}            Total: ${(total + tip20):.2f}')