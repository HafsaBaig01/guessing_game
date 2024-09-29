import random
def play_game():
    #Generate random number between 1 to 50
    computerGuess = random.randrange(1,50)

    #Allow the user 5 attempts
    for attempt in range(1,6):
        userGuess = int(input(f"Attempt {attempt}/5 - Enter Your Guess:  "))

        if userGuess>computerGuess:
            print("Your Guess is too high!")
        elif userGuess<computerGuess:
            print("Your Guess is too low!")
        else:
            print(f"Congratulations! You Guessed it right. The correct numbber is {computerGuess}")
            break  #exit the loop if guess is correct
    else:
        print(f"Sorry, you've used all your tries! the correct number was {computerGuess}. Better luck next time!")