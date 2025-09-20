import random as r

"""
Lab4_kbreinholt_add.py
Kaden Breinholt
This program was meant to be a virtual 'Card Dealer' that is given a number representing the
number of cards to be dealt, and dealing that number of cards. It was meant originally to be
relatively simplistic, but I thought I could do better, so I made sure the cards do not repeat
and that the cards are displayed as names instead of codes. I also added a 'cards used' list
that for this program in its current state is just a copy of the hand dealt, but was meant to
be used if this program was ever expanded to deal multiple hands (in which case, repeating cards
between hands would not be good).
Sat Sep. 20th
"""

cards = ["The Ace of ", "The Two of ", "The Three of ", "The Four of ", "The Five of ", "The Six of ", "The Seven of ", "The Eight of ", "The Nine of ", "The Ten of ", "The Jack of ", "The Queen of ", "The King of "]
suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
cards_used = []
hand_dealt = []

deal_num = int(input("\nHow many cards should be dealt per hand?\n"))
while deal_num > 0:
        card_drawn = cards[r.randint(0, 12)] + (suits[r.randint(0, 3)])
        if card_drawn not in cards_used:
                hand_dealt.append(card_drawn)
                cards_used.append(card_drawn)
                deal_num -= 1
print(f"\nThe cards you were Dealt are:\n{hand_dealt}\n")