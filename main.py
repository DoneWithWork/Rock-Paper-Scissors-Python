# Import random module
import random


# Reference
# rock 1 beats scissors 2
# scissors 2 beats paper 3
# paper 3 beats rock 1

# Main Game Loop
def main():
    # Some print statements
    print("Welcome to Rock Paper Scissors")
    print("Rock = 1")
    print("Scissors = 2")
    print("Paper = 3")

    choice = int(input("What is your pick? (1/2/3) : "))  # Getting Player input
    computersChoice = random.randint(1, 3)  # Computer picks a random number from 1-3

    # Basic Logic
    if choice == computersChoice:  # If Player's choice is equal to the computer's choice
        print("Draw!")  # Print some simple output statements
        print("The computer picked", computersChoice)  # Print the computer's choice
        restart()  # Restart the game
    elif choice == 1 and computersChoice == 2:  # Else if computer pick scissors and player choose rock
        print("You won!!")  # Print some simple output statements
        print("The computer picked", computersChoice)  # Print the computer's choice
        restart()  # Restart the game
    elif choice == 2 and computersChoice == 3:  # Else if computer picks paper and player picks scissors
        print("You won!!")  # Print some simple output statements
        print("The computer picked", computersChoice)  # Print the computer's choice
        restart()  # Restart the game
    elif choice == 3 and computersChoice == 1:  # Else if computer picks rock and player picks paper
        print("You won!!")  # Print some simple output statements
        print("The computer picked", computersChoice)  # Print the computer's choice
        restart()  # Restart the game
    elif computersChoice == 1 and choice == 2:  # Else if computer picks rock and player picks scissors
        print("You lost!")  # Print some simple output statements
        print("The computer picked", computersChoice)  # Print the computer's choice
        restart()  # Restart the game
    elif computersChoice == 2 and choice == 3:  # Else if computer picks scissors and player picks paper
        print("You lost!")  # Print some simple output statements
        print("The computer picked", computersChoice)  # Print the computer's choice
        restart()  # Restart the game
    elif computersChoice == 3 and choice == 1:  # Else if computer picks paper and player picks rock
        print("You lost!")  # Print some simple output statements
        print("The computer picked", computersChoice)  # Print the computer's choice
        restart()  # Restart the game
    else:  # Else, if the player inputs an incorrect statements
        print("Please enter a correct input!!")  # Print some simple output statements
        main()  # Repeat Main Loop


# A function to restart the game
def restart():
    replay = str(input("Would you like to replay the game? (y/n): "))  # Getting player input
    if replay == "y":  # If the input is "y"
        main()  # Start main loop again
    elif replay == "n":  # Else If the input is "n"
        print("Thank you for playing. Goodbye!")
        quit()  # Quit the programme
    else:  # If the input is not "y" or "n"
        print("Please enter a correct input!")
        restart()  # Repeat this function


# While loop to keep game going
while True:
    main()
