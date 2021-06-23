# importing random
import random

# # making a list of words and assing word to a random word in the list
# words = ["helloworld", "coding", "python", "programmer", "computer", "learning", "hangman"]
# word = random.choice(words)

# or students can use a large txt file for more variety of words
with open("words.txt") as f:
    word_list = f.read().splitlines()
word = word_list[random.randint(0, len(word_list)-1)].lower()

# instantiating variables
lives = 5
guesses = []
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
    for i in range(len(wordCompletion)):
        print(wordCompletion[i], end=" ")
    guess = str(input("\n\nGuess a letter or word: "))
    if guess not in guesses:
        if guess == word:
            finished = True
        else:
            if guess in word:
                print("\nCorrect!")
                wordList = list(word)
                for g in guess:
                    for i in range(len(wordList)):
                        if wordList[i] == g:
                            wordCompletion[i] = g
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

# printing the outcome -- whether they lost or won
print(f"\n\nYou {outcome}! The word was \"{word}\"")