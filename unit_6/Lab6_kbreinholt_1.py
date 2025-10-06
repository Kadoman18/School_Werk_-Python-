"""
Create a dictionary of at least four key-value pairs. Each key should be a unique username and,
the associated value, a password, all character strings. The user should be asked to provide their
username, then check if the username is in the database/dictionary. Exit if it is not. If a valid
username, the user is asked to provide their password. The program will assign a security level,
starting at the top value of 1. Guests should be allowed to login with the name “guest” and the
password “guest”, with the lowest security level. The program should end with a greeting to the
username and let them know their security level.
"""
## I had a lot of fun with this one:)
## I was confused about the 'starting at a top value of 1' part but made it so the
## clearance level can be modified in the accounts dictionary.

accounts = {
        "KookyDummy1966": {"password": "MikeyBoy22!", "clearance": 1},
        "LyvLongandProsper": {"password": "Nerdbird67!?", "clearance": 1},
        "GuyFieriStan": {"password": "BadtotheBone1997?", "clearance": 1},
        "Kadoman": {"password": "Kb2001047992?", "clearance": 1},
        "guest": {"password": "guest", "clearance": 0}
}
username = str(input("\nWelcome to the Sunny Meadows Security System.\nPlease Sign-in.\n\nUsername: "))
while username not in accounts.keys():
        username = str(input("\nUsername Incorrect. Please try again.\nUsername: "))
password = str(input("Password: "))
while password != accounts[username]["password"]:
        password = str(input("\nPassword Incorrect. Please try again.\nPassword: "))
print(f"\nClearance Level: {accounts[username]["clearance"]}\nWelcome, {username}.\n\n")
