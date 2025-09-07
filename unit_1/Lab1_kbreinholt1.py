'''
You are the owner of a restaurant.
Ask one of your employees to write
a program which takes a total from
a bill for dinner and prints out
suggestions for a 15% tip and 20%
tip. Then gives the total for the meal
with the 15% tip and another with the 20%
tip. Use F-strings.
'''
total = float(input())
tip15 = total * 0.15
tip20 = total * 0.2
print(f'For todays meal would you like to tip 15%, which would be ${tip15:.2f} for a total cost of ${(total + tip15):.2f}, or 20%, which would be ${tip20:.2f} for a total cost of ${(total + tip20):.2f}')