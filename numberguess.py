"""This is a program that generates a
random number from a dice roll"""

from random import randint
from time import sleep


def get_user_guess():
    return int(raw_input("Enter a guess: "))


def roll_dice(number_of_sides):
    roll1 = randint(1, number_of_sides)
    roll2 = randint(1, number_of_sides)
    total = roll1 + roll2
    max_val = number_of_sides * 2
    print "Maximum roll: %s" % max_val
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > total:
        print "Fuck you! Your guess was too high!"
        return
    else:
        print "Rolling..."
        sleep(2)
        print "%s and %s make %s" % (roll1, roll2, total)
        return


roll_dice(10)
