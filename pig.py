# Mengqian Wu 
# I did the work alone 

from random import randint
import random




        
def print_instructions():
    '''Prints the rules of the game.
    '''
    intro = """
    Let's play pig!  Here are the rules:
    - You and the computer will take turns rolling a six-sided die as many times as you want, or until you roll a 6.
    - Each number you roll, except a 6, will be added to your score for that turn; but if you roll a 6, your score for that turn will be a 0, and your turn will end.
    - At the end of each turn, the score for that turn is added to your total score. The first player to reach or exceed 50 wins.
    - If you and the computer are tied with 50 or more, you'll each get another turn until the tie is broken.
    - The computer will go first! 
    """
    print(intro)
    

def computer_move(computer_score, human_score):
    '''Has the computer roll some number of times, displays the result of each roll, and
    returns the result (either 0 or the total value of the rolls).
    Uses the given arguments to play more intelligently.
    '''

    # create loop to roll the die to get random results and update the score 
    while True:
        #call the roll() function to roll the die
        result = roll()
        print("The computer rolled a {}.".format(result))

        # if rolling a 6, the loop breaks, and show the current status
        if result == 6:
            show_current_status(computer_score, human_score)
            break

        # sum up the score     
        computer_score += result 
   
    return computer_score



def human_move(computer_score, human_score):
    '''Repeatedly asks whether the user wants to roll again and displays the result of each roll.

    - If the user chooses to roll again, and DOES NOT roll a 6, this function adds the roll
    to the total of the rolls made during this move.
    - If the user chooses to roll again, and DOES roll a 6, the function returns 0.
    - If the user chooses not to roll again, the function returns the total of the rolls made during this move.
    '''
    # create question
    prompt = 'Do you want to roll? (y/n)'
    
    # create loop for human roll
    while True:
        
        # get the response (y/n)
        ans = ask_yes_or_no(prompt)
        game_over = is_game_over(computer_score, human_score)

        if ans == False:
            print('Let us stop here.')
            show_current_status(computer_score, human_score)
            break
        
        elif ans == True:
            result = roll()

            # show the result for each roll
            print("You rolled a {}.".format(result))

            # stop when it reaches 6
            if result == 6:
                break
        
            # sum up the human score for this round 
            human_score += result 
            show_current_status(computer_score, human_score)
        
    
        else:
            game_over = True
            show_final_results(computer_score, human_score)
            break

        
    return human_score

def is_game_over(computer_score, human_score):
    '''Returns True if either player has 50 or more, and the players are not tied,
    otherwise it returns False.
    '''
    game_over = False
    

    # tie
    if computer_score == human_score:
        game_over = True
    
    # computer win
    elif computer_score >= 50:
        game_over = True
    
    # human win
    elif human_score >= 50:
        game_over = True

    else:
        game_over = False
    
    return game_over

def roll():
    '''Returns a random number in the range 1 to 6, inclusive.
    '''
    roll = random.randint(1, 6)

    return roll
    
def ask_yes_or_no(prompt):
    '''Prints the given prompt as a question to the user, for example, "Roll again? (y/n) ".

    - If the user responds with a string whose first character is 'y' or 'Y', returns True.
    - If the user responds with a string whose first character is 'n' or 'N', returns False.
    - Any other response causes the question to be repeated until the user provides an acceptable response.
    '''

    # ask users whether they want to roll
    ans = input(prompt)
    if ans[0] in {'y' or 'Y'}:
        return True

    elif ans[0] in {'n' or 'N'}:
        return False
        
    else: 
        print('Type wrong! Do you want to roll? (y/n) ')

          

def show_current_status(computer_score, human_score):
    '''Tells the user both her current score and the computer's score, and how far
    behind (or ahead) she is, or if there is a tie.
    '''
    # human's score higher
    if computer_score < human_score:
        dif = human_score - computer_score
        current = "The computer's score is {} and your score is {}. (You are {} points ahead of the computer)".format(computer_score, human_score, dif)
        print(current)
    # tie
    elif computer_score == human_score:
        current = "The computer's score is {} and your score is {}. You are tied".format(computer_score, human_score)
        print(current)

    # computer's score higher
    elif computer_score > human_score:
        dif = computer_score - human_score
        current = "The computer's score is {} and your score is {}. (You are {} points behind the computer.)".format(computer_score, human_score, dif)
        print(current)
    
    else:
        pass

def show_final_results(computer_score, human_score):
    '''Tells the user whether she won or lost, and by how much.
    '''
    # if human wins, then human wins
    if computer_score < human_score:
        
        dif = human_score - computer_score
        final = "The computer's score is {} and your score is {}. (You are {} points ahead of the computer.) You won by {} points!".format(computer_score, human_score, dif, dif)
    
    # if computer wins, then human has another round to roll because computer starts the game
    else:
        last = roll()
        print('You have the last round to roll! You roll {}.'.format(last))
        human_score += last
        dif = computer_score - human_score
        final = "The computer's score is {} and your score is {}. (You are {} points behind the computer.) You lose by {} points!".format(computer_score, human_score, dif, dif)
    
    print(final)


def main():

    # tell the rules of game, and start the game 
    print_instructions()

    print("Ready to play? First round is computer\'s game.")
    input('Press Enter to continue...')
   
    game_running = True


    #set initial scores
    human_score = 0
    computer_score = 0

    # start the game 
    while game_running:

        #computer starts the first round 
        computer_score += computer_move(computer_score, human_score)

        #human starts the second round with a permission  
        human_score += human_move(computer_score, human_score)

        #check if we have a winner in this round 
        if is_game_over(computer_score, human_score) == True:
            show_final_results(computer_score, human_score)
            #game_running = False
            break

 

    

if __name__ == '__main__':
    main()