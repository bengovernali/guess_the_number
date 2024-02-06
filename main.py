import random

##Step 1: Ask user if they want hard or easy mode
##Step 2: Ask user for guess
##Step 3: Compare user guess to number
##Step 3a: If higher, print "Too high". If lower, print "Too low". If correct, print "Correct, you win!"
##Step 3b: If win, ask if user wants to play again
##Step 3c: If not win, reduce amount of guesses by 1
##Step 3d: If amount of guesses = 0, print "No more guesses, you lose!" then ask to play again
##Step 3e: start loop again from step 2
##Step 4: Start loop again from step 1
##Step 5: break while loop to end program

def play_game():
    ##set number to be guessed
    number = random.randint(1, 100)
    
    ##ask for difficulty level and define amount of guesses
    difficulty = input("Would you like to play hard mode (type: 'hard'), or easy mode (type: 'easy'): ?")
    if difficulty == 'hard':
        guessesRemaining = 5
    else:
        guessesRemaining = 10
    
    ##set while loop to run while guessesRemaining > 0
    while guessesRemaining > 0:
        ##prompt user for a guess
        guess = int(input("Please guess a number between 1 and 100: "))

        ##compare guess to number
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low!")
        else:
            print(f"Correct! You win! {number}")
            guessesRemaining = 0
        
        ##reduce remainingGuesses
        guessesRemaining -= 1
    
    ##anounce end of game and ask user if they would like to play again
    playAgain = input("Game Over. Would you like to play again? (y/n): ")

    if playAgain == 'y':
        play_game()
    else:
        ##end game
        return

play_game()


