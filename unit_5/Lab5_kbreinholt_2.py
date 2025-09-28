stix_pix_settings = {"min": 1, "max": 4, "total": 13}
pile = stix_pix_settings["total"]
player = 1
print("\n\tWelcome to Pick Up Sticks.\n\nEach player takes turns picking 1 to 4 sticks from a pile of 13 sticks.\nWhoever picks up the last stick wins.")
while pile > 0:
        print(f"\n\nThere are {pile} stick(s) in the Pile.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        take = int(input(f"Player {player}:\nHow many sticks will you take?\nSticks: "))
        while ((take < stix_pix_settings["min"]) or (stix_pix_settings["max"] < take) or pile < take):
                print(f"\n\nThere are {pile} stick(s) in the Pile.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                take = int(input(f"Player {player}:\nHow many sticks will you take?\nSticks: "))
        pile -= take
        if pile <= 0:
                print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n            Player {player} Wins!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        else:
                player = 1 if player == 2 else 2