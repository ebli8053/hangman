import random

words_list = ["CAT", "MOON", "HAPPY", "PYTHON", "LADYBUG", "DINOSAUR", "CHOCOLATE", "PROGRAMMER"]
incorrect_letters = []

def random_word():
    n = random.randint(0, len(words_list) - 1)
    rand_word_split = list(words_list[n])
    print(rand_word_split)
    correct_letter(rand_word_split)

def choose_word():
    word = input("Enter your word: ").upper()
    word_split = list(word)
    correct_letter(word_split)

def guess_letter(word):
    letter = input("Guess a letter: ").upper()
    while letter in incorrect_letters:
        letter = input("You have already tried this letter.\nGuess a letter: ")
    return(letter in word, letter)

def correct_letter(word_list):
    index = 0
    while len(word_list) > 0 and index < 6:
        guess = guess_letter(word_list)
        if guess[0] == True:
            word_list.remove(guess[1])
            print(hangman(index))
        else:
            incorrect_letters.append(guess[1])
            index += 1
            print(hangman(index))
    if index == 6:
        return loser()
    else:
        return winner()

def hangman(n):
    hangman_0 = (f"----------------\n|   /          |\n|  /           |\n| /\n|/\n|\n|\n|\n|\n|\n|\n|\n|\n")
    hangman_1 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|\n|\n|\n|\n|\n|\n|\n")
    hangman_2 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|              |\n|              |\n|              |\n|\n|\n|\n")
    hangman_3 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\n|            / |\n|           /  |\n|\n|\n|\n")
    hangman_4 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|\n|\n|\n")
    hangman_5 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             /\n|            /\n|           /\n") 
    hangman_6 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             / \ \n|            /   \ \n|           /     \ \n")
    hangman_7 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |x x|\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             / \ \n|            /   \ \n|           /     \ \n")
    
    hangman_list = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6, hangman_7]
    return(hangman_list[n])

def winner():
    print("                             ___  __")
    print("|   |   | |   |   |   |   | |    |  |")
    print(" | | | |  |  | | |   | | |  |--  |-|")
    print("  |   |   | |   |   |   |   |___ |  |")
    print("              _____ ")
    print("             | O O |")
    print("             |  U  |")
    print("             |_____|")

def loser():
    print(" ___   __             ___ ")
    print("|     |  |   |   |   |")
    print("|---| |--|  | | | |  |--")
    print("|___| |  | |   |   | |___ ")
    print("   ___         ___  __")
    print("  |   | |   | |    |  |")
    print("  |   |  | |  |--  |-|")
    print("  |___|   |   |___ |  |")
    print("          _____")
    print("         | x x |")
    print("         |  -  |")
    print("         |_____|")
        

random_word()