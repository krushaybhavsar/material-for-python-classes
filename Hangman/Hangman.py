
# word for user to guess
word = "helloworld"

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
    guess = str(input("\n\nGuess a letter or word: "))
    if guess not in guesses:
        if guess == word:
            finished = True
        else:
            if word.find(guess) != -1:
                print("\nCorrect!")
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