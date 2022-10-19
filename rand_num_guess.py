# Created by: Lia Duggan
# Created on: October 19th 2022
# User guesses a number between 0 and 9
# and the program tells the user if
# they guessed correctly or not
import random


def main():
    # Generating the random number
    answer = random.randint(0, 9)

    user_guess = int(input("Enter an Integer: "))

    # Determining whether the answer is correct
    if user_guess == answer:
        print("You guessed correctly!")
    else:
        print(
            "You guessed wrong, The correct answer was",
            answer,
        )


if __name__ == "__main__":
    main()
