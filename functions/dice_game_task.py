# Make a dice game:
import random

# Let's make a game that rolls a dice and picks a winner.

# Start the game with a welcome message and ask if the user is ready to play.

# Get the user's name and start a loop (While loop recommended)

# Use the random library and a method from that library to roll, a number 1-6

# Store the number in a variable

# Do the same for the computer

# Compare the two numbers, whose was bigger? Tell the user! and end the game

computer_dice_roll = True

end_game = False
input('Hello and welcome to the dice game, when you\'re ready enter your name: ')

def dice_roll():
    return random.randint(1, 6)


while end_game is False:
    user_score = dice_roll()
    print(f'Your score is: {user_score}')
    comp_score = dice_roll()
    print(f'The Computers score is: {user_score}')
    if user_score > comp_score:
        print(f'Congratulations you won!')
    elif comp_score > user_score:
        print('Unlucky! You Lose This Time')
    elif comp_score == user_score:
        print('It\'s a tie!')
    end_game = True




# Now add functionality to the game. Let the User and the CPU roll until one gets to 30.
# The one that gets there first is the winner!

# Bonus: Want to play again?
