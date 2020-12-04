'''
    Hangman_Terminal
    by Johnathan Davidow
    Visit https://johnathandavidow.000webhostapp.com for more.
'''

import getpass
import time
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
        print("You win. The word was: "+word)
        return False

    # Detects loss
    if(game_state == 6):
        gallows = open(r"resources/gallows"+str(game_state)+".txt")
        print(gallows.read())
        gallows.close()
        print("You lose. The word was: "+word)
        return False
    
    return True

# Game against another player
def gameHuman(word):
    game_state = 0;
    running = True
    word_array = ["_"] * len(word)
    guessed_characters = ""
    while(running):
        gallows = open(r"resources/gallows"+str(game_state)+".txt")
        print(gallows.read())
        gallows.close()
        print("Guessed characters:"+guessed_characters)
        choice = ord(input("1. Guess character\n2. Guess word\n"))-48
        if(choice <= 1):
            char = input("Character: ")[0]
            if(char in word):
                for j in range(len(word)):
                    if(char == word[j]):
                        word_array[j] = char
                        print(char+" was in the word")
                        print("Chances remaining: "+str(game_state+7))

                if(char not in guessed_characters):
                    guessed_characters += " "+char
            else:
                print(char+" was not in the word")
                print("Chances remaining: "+game_state+7)
                if(char not in guessed_characters):
                    guessed_characters += " "+char
                game_state += 1;
            for i in word_array:
                print(i, end="")
            print()
        else:
            guess = input("Input what you think the word is: ")
            if guess == word:
                c = 0
                while(c < len(word)):
                    word_array[c] = word[c]
                    c += 1
            else:
                game_state += 1

        # Detects win
        running = checkState(game_state, word_array, word)


# Game against the computer
def gameCPU():
    dictionary = open(r"resources/dictionary.txt")
    lines = dictionary.readlines()
    word = random.choice(lines) 
    game_state = 0;
    running = True
    word_array = ["_"] * (len(word)-1)
    guessed_characters = ""
    while(running):
        gallows = open(r"resources/gallows"+str(game_state)+".txt")
        print(gallows.read())
        gallows.close()
        print("Guessed characters:"+guessed_characters)
        choice = ord(input("1. Guess character\n2. Guess word\n"))-48
        if(choice <= 1):
            char = input("Character: ")[0]
            if(char in word):
                for j in range(len(word)):
                    if(char == word[j]):
                        word_array[j] = char

                if(char not in guessed_characters):
                    guessed_characters += " "+char
            else:
                print(char+" was not in the word")
                if(char not in guessed_characters):
                    guessed_characters += " "+char
                game_state += 1;
            for i in word_array:
                print(i, end="")
            print()
        else:
            guess = input("Input what you think the word is: ")
            if guess == word:
                c = 0
                while(c < len(word)):
                    word_array[c] = word[c]
                    c += 1
            else:
                game_state += 1

        # Detects win
        running = checkState(game_state, word_array, word)


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