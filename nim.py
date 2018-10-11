#(20 points) The game of Nim. 
# This is a well-known game with a number of variants. 
# The following variant has an interesting winning strategy. 
# Two players alternately take marbles from a pile. 
# In each move, a player chooses how many marbles to take. 
# The player must take at least one but at most half of the 
# marbles. Then the other player takes a turn. The player 
# who takes the last marble loses.

# Write a program in which the computer plays against a 
# human opponent. Generate a random integer between 10 and 
# 100 to denote the initial size of the pile. Generate a 
# random integer between 0 and 1 to decide whether the 
# computer or the human takes the frst turn. Generate a 
# random integer between 0 and 1 to decide whether the 
# computer plays smart or stupid. In stupid mode the computer
#  simply takes a random legal value (between 1 and n/2) from
#  the pile whenever it has a turn. In smart mode the computer
#  takes off enough marbles to make the size of the pile a power
#  of two minus 1—that is, 3, 7, 15, 31, or 63. That is always 
# a legal move, except when the size of the pile is currently 
# one less than a power of two. In that case, the computer makes
#  a random legal move.

# You will note that the computer cannot be beaten in smart 
# mode when it has the frst move, unless the pile size happens 
# to be 15, 31, or 63. Of course, a human player who has the 
# frst turn and knows the winning strategy can win against the 
# computer.



# You need to replace 'pass' with your code

from random import randint
from math import log

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

# Create the initial pile, determine the starting player and the computer's
# strategy.
pile = randint(10, 100)
turn = randint(0, 1)
strategy = randint(0, 1)


def nim():
    """
    return True if the winner is human, False if winner is computer.
    """
    # While the game is still being played.
    pile = randint(10, 100)
    HUMAN = 0
    COMPUTER = 1
    turn = randint(0, 1)
    SMART = 0
    DUMB = 1    
    strategy = randint(0, 1)
    take = 0
    while pile > 0:
        if turn == COMPUTER:
            if pile == 1:
                # Take the last marble.
                take = 1
                pile = pile - take
                if pile == 0:
                    return True
            elif strategy == DUMB:
                # Take a random, legal number of marbles from the pile. At least 1, at most half of pile.
                # 1 and n/2
                for take in range(pile):
                    pile = int(pile / 2)
                    take = randint(1, pile)
                    pile = pile - take
                    if pile == 0:
                        return True
                    elif pile == 1:
                        return False
            elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                # The computer is smart, but can't make a smart move.
                # Take a random, legal number of marbles from the pile.
                for take in range(pile):
                    pile = int(pile / 2)
                    take = randint(1, pile/2)
                    pile = pile - take
                    if pile == 0:
                        return True
                    elif pile == 1:
                        return False
            else:
                # The computer is smart and can make a smart move.
                # Take marbles so that the pile will be be a power of 2, minus 1.
                for take in range(pile):
                    take = log(pile) + 1
                    pile = pile - take
                    if pile == 0:
                        return True
                    elif pile == 1:
                        return False
            # Update pile
            pile = pile - take
            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            # take is the variable you might need above
            turn = HUMAN

        elif turn == HUMAN:
            print("Your turn.   The pile currently has", pile, "marbles in it.")

            take = int(input("How many marbles will you take? "))
            # Force the user to take a legal number of marbles.
            if take != randint(1, int(pile/2)):
                print("Error, select legal number of marbles")

            # Update pile
            pile = pile - take
            print("Now the pile has", pile, "marbles in it.\n")
            turn = COMPUTER

    return turn == COMPUTER

if nim():
    print("You Won!")
else:
    print("The computer won!")
