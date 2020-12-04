'''
    Hangman_Terminal
    by Johnathan Davidow
    Visit https://johnathandavidow.000webhostapp.com for more.
'''

# For hiding the secret word
import getpass

# For dramatic pauses in the title
import time

# For the computer to choose a word
import random

# Welcome message
welcome_text = open(r"resources/welcome.txt")
title = open(r"resources/title.txt")
print(welcome_text.read())
time.sleep(1)
print(title.read())
welcome_text.close()
title.close()
time.sleep(1)

global running
running = False

def checkState(game_state, word_array, word):
    # Detects win
    if "_" not in word_array:
        gallows = open(r"resources/gallowsWin.txt")
        print(gallows.read())
        gallows.close()
        print(f"You win. The word was: {word}")
        return False

    # Detects loss
    if(game_state == 6):
        gallows = open(r"resources/gallows"+str(game_state)+".txt")
        print(gallows.read())
        gallows.close()
        print(f"You lose. The word was: {word}")
        return False
    
    return True

def playGame(word):
    # So the screen doesn't feel too disorganized
    edge = "-" * 100

    # The state will determine weather or not the game should end
    game_state = 0;
    
    running = True

    # Initializes and array the size of the word
    word_array = ["_"] * len(word)

    guessed_characters = ""

    while(running):
        print(edge)
        gallows = open(r"resources/gallows"+str(game_state)+".txt")
        print(gallows.read())
        gallows.close()
        print(f"Guessed characters:{guessed_characters}")
        choice = ord(input("1. Guess character\n2. Guess word\n"))-48
        if(choice <= 1):
            char = input("Character: ")[0]
            print(edge)
            if(char in word):
                for j in range(len(word)):
                    if(char == word[j]):
                        word_array[j] = char
                        print(f"{char} was in the word")
                        print(f"Chances remaining: {str(7-game_state)}")

                if(char not in guessed_characters):
                    guessed_characters += f" {char}"
            else:
                print(f"{char} was not in the word")
                print(f"Chances remaining: {str(7-game_state)}")
                if(char not in guessed_characters):
                    guessed_characters += f" {char}"
                game_state += 1;
            for i in word_array:
                print(i, end="")
            print()
        else:
            guess = input("Input what you think the word is: ")
            if guess == word:
                for c in range(len(word)):
                    word_array[c] = word[c]
            else:
                print(f"{guess} was not the word")
                game_state += 1

        # Detects win
        running = checkState(game_state, word_array, word)

# Game against another player
def gameHuman(word):
    playGame(word)


# Game against the computer
def gameCPU():
    # Opens text file containing random words
    dictionary = open(r"resources/dictionary.txt")

    # Adds each line to an array
    lines = dictionary.readlines()

    # Chooses one of the lines at random
    word = random.choice(lines) 

    # Cuts off the new line character
    word = word[:len(word)-1]

    playGame(word)


# Setup the game
def setup():
    try:
        choice = int(input("1. PvP\n2. PvCPU (VERY DIFFICULT)\n"))
    except Exception as error:
        print("Error:", error)
        setup()
    else:
        if(choice > 1):
            gameCPU()
        else:
            try:
                # Hides the input
                word = getpass.getpass("Word to guess: ")
                gameHuman(word)
            except Exception as error:
                print("Error:", error)
                setup()
setup()