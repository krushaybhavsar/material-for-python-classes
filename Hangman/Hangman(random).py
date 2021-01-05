# importing random
import random

# making a list of words and assing word to a random word in the list
words = ["helloworld", "coding", "python", "programmer", "computer", "learning", "hangman"]
word = words[random.randint(0, len(words))]

# instantiating variables
wordSoFar = ""
lives = 5
guesses = []
correctGuesses = []
wordCompletion = []
finished = False
outcome = "won"

# asking user their name
name = str(input("Welcome to Hangman! What is your name? "))
print(f"Hello {name}!")

# generating dashes for not yet guessed letters
for i in range(len(word)):
    wordCompletion.append("_")

# game logic
while finished == False:
    guess = str(input("\n\nGuess a letter or word: "))
    if guess not in guesses:
        if guess == word:
            finished = True
        else:
            if guess in word:
                print("\nCorrect!")
                correctGuesses.append(guess)
                wordList = list(word)
                for i in range(len(wordList)):
                    if wordList[i] == guess:
                        wordCompletion[i] = guess
            else:
                print("\nIncorrect!")
                lives -= 1
                if lives == 0:
                    finished = True
                    outcome = "lost"
            guesses.append(guess)
            print(f"Guesses so far: {guesses}")
            print(f"Lives left: {lives}\n")
    else:
        print("\nYou already guessed that!")
    for i in range(len(wordCompletion)):
        print(wordCompletion[i], end="")

# printing the outcome -- whether they lost or won
print(f"\n\nYou {outcome}! The word was \"{word}\"")