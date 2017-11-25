"""Welcome to th rock paper scissors game"""

from random import randint
from time import sleep


options = ['R', 'P', 'S']
winning_picks = {'R': 'S', 'P': 'R', 'S': 'P'}
lost = "You lost!"
win = "You win!"


def decide_winner(user_choice):
    print "User picks %s" % user_choice
    print "Computer computing..."
    sleep(1)
    computer_choice = options[randint(0,2)]
    print "Computer picks %s" % computer_choice
    if computer_choice == user_choice:
        return "Tie!"
    elif winning_picks[user_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"


user_choice = raw_input("Pick R, P, or S to play: ")
# user_choice = 'R'
print decide_winner(user_choice)
