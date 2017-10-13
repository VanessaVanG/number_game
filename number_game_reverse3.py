import random
import sys

#Find the upper and lower bounds
def max_min(too_high, too_low):
    if (too_high):
        upper = min(too_high) - 1
    else:
        upper = 10
    if (too_low):
        lower = max(too_low) + 1
    else:
        lower = 1
    return lower, upper

#comp makes a new guess
def new_guess(too_high, too_low):
    #get upper and lower bounds
    bounds = max_min(too_high, too_low)        
    #comp makes a new guess
    try:
        guess = random.randint(bounds[0], bounds[1])
    except ValueError:
        print("You're cheating! No more game for you!")
        #game()
        sys.exit()
        #break
    return guess

#game function
def game(): 
    #make lists
    too_high = []
    too_low = []
    #get a random number
    guess = random.randint(1, 10)
    #Welcome
    print("Think of a number between 1 and 10. I have 4 chances to guess it! Don't cheat!! \n ")
    while len(too_high) + len(too_low) < 4:
        #the computer gives its guess
        print("Is your number {}?".format(guess))
        choice = input('''Enter a for yes 
Enter b for too high
Enter c for too low
    > ''').lower()

        #correct
        if choice == 'a':
            print("Yay! I won!!! I guessed your secret number {}!!!.".format(guess))
            break
        #too high    
        elif choice == 'b':
            #add guess to too_high list
            too_high.append(guess)
            print("So {} is too high...".format(guess))
            #comp guesses again
            guess = new_guess(too_high, too_low)        
        #too low
        elif choice == 'c':
            #add guess to too_low list
            too_low.append(guess)
            print("So {} is too low...".format(guess))
            #comp guesses again
            guess = new_guess(too_high, too_low)            
        #invalid choice
        else:
            print("Invalid entry.")
    #Lose
    else:
        print("I lost!")

    #Let people play again
    play_again = input("Would you like to play again? Y/n ").lower()
    if play_again != 'n':
        game()
    else:
        print("Okay, thanks for playing! Bye!")

game()




        
