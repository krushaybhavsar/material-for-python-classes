'''This is a set of Python challenges that helps 
students gain practice and confidence in their skills.'''

# HELPFUL LINK
# https://www.practicepython.org/

############### PRIME OR COMPOSITE ###############
'''
TASK: create a program that asks the user for an
integer input and prints out whether the number
is prime, composite, or neither. CHALLENGE: Edit 
the program to make use of functions.
'''
# num = int(input("Input a number: "))
# if num > 1:
#     for i in range (2, num):
#         if num % i == 0:
#             print(f"{num} is a composite number")
#             break
#         if i == num - 1:
#             print(f"{num} is a prime number")
# else:
#     print(f"{num} is neither prime nor composite")
##################################################



############### FIBONACCI SEQUENCE ###############
'''
TASK: create a program that asks the user for an
integer number and prints out the fibonacci
sequence for that many terms (the fibonacci sequence
is a sequence of numbers in which the next term is
the sum of the previous two terms). CHALLENGE: Edit
the program to make use of functions.
'''
# num = int(input("Input a number: "))
# previous2 = 0
# previous1 = 1
# current = previous1 + previous2
# for i in range(num):
#     print(current, end=" ")
#     current = previous1 + previous2
#     previous2 = previous1
#     previous1 = current 
##################################################



################ GUESS THE NUMBER ################
'''
TASK: create a program that asks the user to guess
an integer number and prints out whether or not the
user guessed right. Be sure to keep the program
running until the user guesses right CHALLENGE:
When the user wins, print out the number of tries.
'''
# import random
# guess = int(input("Guess a number: "))
# actual = random.randint(1, 10) # You can tweak the range
# while guess != actual:
#     print("Incorrect!", end=" ")
#     guess = int(input("Guess another number: "))
# print(f"Correct! The number was {actual}!")
##################################################



############## ROCK PAPER SCISSORS ###############
'''
TASK: create a program that asks the user to choose
either rock, paper, or scissors. The computer will
then choose a random choise out of the three options
and print out the outcome of the rounds (either the 
computer won or the user won). At the end of each 
round ask the user if they want to continue playing.
Depending on what they say, either exit or continue
the game.
'''
# import random

# comp_score = 0
# user_score = 0

# def play_game():
#     comp_choice = random.choice(["rock", "paper", "scissors"])
#     user_choice = input("Choose 'rock', 'paper', or 'scissors' >> ")
#     if (comp_choice == "rock" and comp_choice != user_choice):
#         if (user_choice == "paper"):
#             print_end_of_round(comp_choice, "Won")
#         else:
#             print_end_of_round(comp_choice, "Lost")
#     elif (comp_choice == "paper" and comp_choice != user_choice):
#         if (user_choice == "scissors"):
#             print_end_of_round(comp_choice, "Won")
#         else:
#             print_end_of_round(comp_choice, "Lost")
#     elif (comp_choice == "scissors" and comp_choice != user_choice):
#         if (user_choice == "rock"):
#             print_end_of_round(comp_choice, "Won")
#         else:
#             print_end_of_round(comp_choice, "Lost")
#     else:
#         print_end_of_round(comp_choice, "Tied")

# def print_end_of_round(comp_choice, outcome):
#     print(f"I chose {comp_choice}. You {outcome}!")
#     if outcome == "Won":
#         user_score += 1
#     elif outcome == "Lost":
#         comp_score += 1
#     answer = input("The score is:\nComputer: {}Would you like to play again? (y/n) >> ")
#     if answer == "y":
#         play_game()
#     elif answer != "n":
#         print_end_of_round(comp_choice, outcome)

# play_game()

################# LIST EXERCISE ##################
'''
TASK: Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that
contains only the elements that are common between
the lists (without duplicates). Make sure your
program works on two lists of different sizes.
'''
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]
# c = []

# for item in a:
#     if item in b and item not in c:
#              c.append(item)
# print(c)
##################################################
