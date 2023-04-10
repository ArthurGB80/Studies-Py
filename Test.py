import random

while True:
    # generate a random number between 1 and 100
    num = random.randint(1, 100)
    
    # prompt the user for a guess
    guess = int(input("Guess the number between 1 and 100: "))
    attempts = 1
    
    # loop until the user guesses the correct number
    while guess != num:
        if guess < num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1
    
    # print a message congratulating the user on guessing the correct number and the number of attempts it took
    print(f"Congratulations! You guessed the number {num} in {attempts} attempts.")
    
    # ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
