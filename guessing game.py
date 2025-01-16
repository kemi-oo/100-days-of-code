import random
import guessing_game_art
NUMBER_RANGE = range(1, 101)
NUMBERS = []
for n in NUMBER_RANGE:
    NUMBERS.append(n)
num = random.choice(NUMBERS)

easy_attempt = 10
hard_attempt = 5


    
   
    

def reduce_attempt(attempts):
            return attempts - 1

def guess_game():
        player_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if player_choice == 'easy':
            attempts = easy_attempt 
        elif player_choice == 'hard':
            attempts = hard_attempt
        else:
            print("invalid choice")
        print(f"You have {attempts} attempts remaining to guess the number")
            
        while attempts > 0:
                player_guess = int(input("Make a guess: "))
                if player_guess == num:
                    print(f"You got it! the answer was {num}")
                    break
                elif player_guess < num:
                    print("Too low.\nGuess again") 
                     
                elif player_guess > num:
                    print("Too high.\nGuess again")
                
                 
                attempts = reduce_attempt(attempts)
                if attempts > 0:  
                   print(f"You have {attempts} attempts remaining to guess the number")    
                else:
                    print("You have run out of guesses. Refresh the page to run again")
                    break
def play_game():
    print(guessing_game_art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100") 
    guess_game()     
play_game() 
 