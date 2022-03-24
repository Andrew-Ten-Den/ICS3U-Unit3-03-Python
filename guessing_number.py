#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: March 2022
# This program lets the user guess a number between 0 and 9


import constants


def main():
    # this function lets the user guess a number between 0 and 9

    # input
    number_guessed = int(input("Enter a number between 0 and 9: "))

    # process & output
    if number_guessed == constants.SET_NUMBER:
        print("You guessed correct!")
        print("")
        print("Done")

    if number_guessed != constants.SET_NUMBER:
        print("You guessed wrong!")
        print("")
        print("Done")


if __name__ == "__main__":
    main()
